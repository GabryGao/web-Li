import unittest
from pathlib import Path

import yaml


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]


class TeamCopyTest(unittest.TestCase):
    def test_co_advisor_labels_use_owner_supplied_short_forms(self):
        members = yaml.safe_load(
            (REPOSITORY_ROOT / "_data" / "team_members.yml").read_text()
        )
        advising = {member["name"]: member.get("advising") for member in members}

        self.assertEqual(
            advising["Shunfa Zhao"],
            "Co-advised with Prof. Chi Man Pun@U Macau",
        )
        self.assertEqual(
            advising["Jiahe Chen"],
            "Co-advised with Prof. Lansheng Han@HUST",
        )
        self.assertEqual(
            advising["Di Xu"],
            "Co-advised with Prof. Lansheng Han@HUST",
        )


if __name__ == "__main__":
    unittest.main()
