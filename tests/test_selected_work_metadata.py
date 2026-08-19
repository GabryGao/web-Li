import unittest
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]


class SelectedWorkMetadataTest(unittest.TestCase):
    def test_selected_work_omits_year_and_places_venue_after_authors(self):
        card = (
            REPOSITORY_ROOT / "_includes" / "publication-card.html"
        ).read_text()

        self.assertNotIn('class="publication-year-label"', card)
        self.assertIn('class="publication-venue"', card)
        self.assertLess(
            card.index('class="publication-authors"'),
            card.index('class="publication-venue"'),
        )
        self.assertLess(
            card.index('class="publication-venue"'),
            card.index('class="publication-actions"'),
        )


if __name__ == "__main__":
    unittest.main()
