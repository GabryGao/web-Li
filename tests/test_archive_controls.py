import subprocess
import unittest
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]


class ArchiveControlsTest(unittest.TestCase):
    def render_head(self, page_source):
        renderer = r"""
require "liquid"
require "yaml"

root = ARGV.fetch(0)
page_source = File.read(File.join(root, ARGV.fetch(1)))
front_matter = page_source.match(/\A---\s*\n(.*?)\n---/m).captures.fetch(0)
page = YAML.safe_load(front_matter)
page["url"] = page.fetch("permalink", "/")
site = YAML.load_file(File.join(root, "_config.yml"))
head = File.read(File.join(root, "_includes", "head.html"))
head = head.gsub(/{% include .*? %}/, "")
puts Liquid::Template.parse(head).render!("site" => site, "page" => page)
"""
        render = subprocess.run(
            ["ruby", "-e", renderer, str(REPOSITORY_ROOT), page_source],
            cwd=REPOSITORY_ROOT,
            capture_output=True,
            text=True,
        )
        self.assertEqual(render.returncode, 0, render.stderr)
        return render.stdout

    def test_team_page_opts_out_of_archiving_without_hiding_from_search(self):
        html = self.render_head("_pages/team.html")

        self.assertIn('<meta name="robots" content="noarchive">', html)
        self.assertNotIn("noindex", html.lower())

    def test_archive_opt_out_does_not_apply_to_other_pages(self):
        html = self.render_head("_pages/about.html")

        self.assertNotIn('<meta name="robots"', html)


if __name__ == "__main__":
    unittest.main()
