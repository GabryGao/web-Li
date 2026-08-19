import unittest
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]


class SelectedWorkMetadataTest(unittest.TestCase):
    def test_selected_work_omits_year_and_venue_metadata(self):
        card = (
            REPOSITORY_ROOT / "_includes" / "publication-card.html"
        ).read_text()

        self.assertNotIn('class="publication-year-label"', card)
        self.assertNotIn('class="publication-venue"', card)


if __name__ == "__main__":
    unittest.main()
