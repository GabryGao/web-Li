import re
import unittest
from pathlib import Path

import yaml


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]


class PublicationAuthorNamesTest(unittest.TestCase):
    def test_publications_do_not_use_initial_only_author_names(self):
        publications = yaml.safe_load(
            (REPOSITORY_ROOT / "_data" / "publications.yml").read_text()
        )
        initial_name = re.compile(r"(?:^|, )([A-Z]{1,2})\.? ([A-Z][A-Za-z-]+)")

        abbreviated = [
            pub["title"]
            for pub in publications
            if initial_name.search(pub["authors"]) or "..." in pub["authors"]
        ]

        self.assertEqual(abbreviated, [])


if __name__ == "__main__":
    unittest.main()
