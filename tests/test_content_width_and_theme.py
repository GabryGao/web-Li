import re
import unittest
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]


def rule_for(stylesheet: str, selector: str) -> str:
    match = re.search(rf"{re.escape(selector)}\s*\{{(?P<body>[^}}]*)\}}", stylesheet)
    if match is None:
        return ""
    return match.group("body")


class ContentWidthAndThemeTest(unittest.TestCase):
    def test_publication_rows_use_the_full_content_width(self):
        stylesheet = (
            REPOSITORY_ROOT / "_sass" / "components" / "_publication.scss"
        ).read_text()

        self.assertIn("max-width: none", rule_for(stylesheet, ".publication-item"))

    def test_research_hero_uses_the_full_content_width(self):
        html = (REPOSITORY_ROOT / "_pages" / "research.html").read_text()
        stylesheet = (
            REPOSITORY_ROOT / "_sass" / "layouts" / "_research.scss"
        ).read_text()

        self.assertIn('class="page-hero research-page-hero"', html)
        self.assertIn("max-width: none", rule_for(stylesheet, ".research-page-hero h1"))
        self.assertIn(
            "max-width: none", rule_for(stylesheet, ".research-page-hero p:last-child")
        )

    def test_publication_links_follow_the_active_theme(self):
        stylesheet = (
            REPOSITORY_ROOT / "_sass" / "components" / "_publication.scss"
        ).read_text()

        self.assertIn("color: var(--accent)", stylesheet)
        self.assertIn("color: var(--accent-hover)", stylesheet)
        self.assertNotIn("#0000ee", stylesheet)
        self.assertNotIn("#0000b8", stylesheet)


if __name__ == "__main__":
    unittest.main()
