import unittest
from pathlib import Path
import yaml


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]


class PublicationsTextLayoutTest(unittest.TestCase):
    def test_publications_render_as_year_grouped_text_list(self):
        html = (REPOSITORY_ROOT / "_pages" / "publications.html").read_text()
        publications = yaml.safe_load(
            (REPOSITORY_ROOT / "_data" / "publications.yml").read_text()
        )

        self.assertIn('class="publication-year"', html)
        self.assertIn('class="publication-list"', html)
        self.assertIn('class="publication-item"', html)
        self.assertNotIn('class="publications-scholar-link"', html)
        self.assertNotIn('Google Scholar Page', html)
        self.assertIn('class="publication-title-link"', html)
        self.assertIn('class="publication-venue"', html)
        self.assertIn('map: "year" | uniq | sort | reverse', html)
        self.assertTrue(all(isinstance(pub["year"], int) for pub in publications))
        self.assertNotIn('class="publication-card"', html)
        self.assertNotIn('id="pubSearch"', html)


if __name__ == "__main__":
    unittest.main()
