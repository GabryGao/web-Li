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
    def test_large_screens_use_a_wider_content_container(self):
        stylesheet = (
            REPOSITORY_ROOT / "_sass" / "base" / "_variables.scss"
        ).read_text()

        self.assertIn("--container-max: 1440px", stylesheet)

    def test_site_declares_a_stable_light_color_scheme(self):
        head = (REPOSITORY_ROOT / "_includes" / "head.html").read_text()
        reset = (
            REPOSITORY_ROOT / "_sass" / "base" / "_reset.scss"
        ).read_text()

        self.assertIn('<meta name="color-scheme" content="only light">', head)
        self.assertIn("color-scheme: only light", rule_for(reset, "html"))

    def test_site_does_not_switch_to_dark_from_system_preferences(self):
        head = (REPOSITORY_ROOT / "_includes" / "head.html").read_text()

        self.assertIn(
            "document.documentElement.setAttribute('data-bs-theme', 'light')",
            head,
        )
        self.assertNotIn("prefers-color-scheme: dark", head)

    def test_favicon_uses_the_square_spais_logo_with_cache_busting(self):
        head = (REPOSITORY_ROOT / "_includes" / "head.html").read_text()

        self.assertIn("/images/spais-logo.png", head)
        self.assertIn("?v=20260820", head)
        self.assertIn('rel="apple-touch-icon"', head)
        self.assertTrue((REPOSITORY_ROOT / "images" / "spais-logo.png").is_file())
        self.assertNotIn("/images/spais-lab.png", head)
        self.assertNotIn("/favicon.svg", head)

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

    def test_about_profile_stacks_its_three_paragraphs_vertically(self):
        html = (REPOSITORY_ROOT / "_pages" / "about.html").read_text()
        stylesheet = (
            REPOSITORY_ROOT / "_sass" / "layouts" / "_home.scss"
        ).read_text()

        self.assertIn('class="section-card about-profile-card"', html)
        self.assertIn(
            "grid-template-columns: 1fr",
            rule_for(stylesheet, ".about-profile-card"),
        )
        self.assertIn(
            "margin-bottom: var(--space-5)",
            rule_for(stylesheet, ".about-profile-card p"),
        )
        self.assertIn(
            "max-width: none", rule_for(stylesheet, ".about-profile-card p")
        )

    def test_professional_services_intro_uses_the_full_card_width(self):
        html = (REPOSITORY_ROOT / "_pages" / "about.html").read_text()
        stylesheet = (
            REPOSITORY_ROOT / "_sass" / "layouts" / "_home.scss"
        ).read_text()

        self.assertIn('class="section-card professional-services-card"', html)
        self.assertIn(
            "max-width: none",
            rule_for(stylesheet, ".professional-services-card > p:first-child"),
        )

    def test_selected_work_is_a_two_column_plain_text_list(self):
        stylesheet = (
            REPOSITORY_ROOT / "_sass" / "components" / "_publication.scss"
        ).read_text()

        self.assertIn(
            "grid-template-columns: repeat(2, minmax(0, 1fr))",
            rule_for(stylesheet, ".selected-pubs"),
        )
        card_rule = rule_for(stylesheet, ".selected-pubs .publication-card")
        self.assertIn("background: transparent", card_rule)
        self.assertIn("border-bottom: 1px solid var(--border-color)", card_rule)
        self.assertIn(
            "max-width: none",
            rule_for(stylesheet, ".selected-pubs .publication-authors"),
        )


if __name__ == "__main__":
    unittest.main()
