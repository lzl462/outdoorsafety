"""Regression checks for the site's intentional document-layout differences."""
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from check_site import DISCLAIMER, MAIN_PAGES, Document, contract_errors


class DocumentContracts(unittest.TestCase):
    def errors(self, label, markup):
        with TemporaryDirectory() as directory:
            path = Path(directory) / "page.html"
            path.write_text(markup, encoding="utf-8")
            return contract_errors(label, Document(path))

    def page(self, container="main", headings="<h1>About</h1>", disclaimer=DISCLAIMER,
             navigation='<a aria-current="page">About</a>'):
        return f"{navigation}<{container}>{headings}</{container}><p>{disclaimer}</p>"

    def test_current_content_layout_passes(self):
        self.assertEqual(self.errors("about.html", self.page()), [])

    def test_missing_main_is_rejected_for_every_expected_main_page(self):
        for label in MAIN_PAGES:
            with self.subTest(page=label):
                self.assertIn(f"{label}: expected one main",
                              self.errors(label, self.page(container="div")))

    def test_duplicate_main_is_rejected(self):
        self.assertIn("about.html: expected one main",
                      self.errors("about.html", self.page() + "<main></main>"))

    def test_missing_or_duplicate_heading_is_rejected(self):
        for headings in ("", "<h1>About</h1><h1>More</h1>"):
            with self.subTest(headings=headings):
                self.assertIn("about.html: expected one h1",
                              self.errors("about.html", self.page(headings=headings)))

    def test_missing_or_duplicate_disclaimer_is_rejected(self):
        for disclaimer in ("", DISCLAIMER + " " + DISCLAIMER):
            with self.subTest(disclaimer=disclaimer):
                self.assertIn("about.html: expected one shared disclaimer",
                              self.errors("about.html", self.page(disclaimer=disclaimer)))

    def test_content_needs_one_current_navigation_item(self):
        for navigation in ("", '<a aria-current="page">A</a><a aria-current="page">B</a>'):
            with self.subTest(navigation=navigation):
                self.assertIn("about.html: expected one current page indicator",
                              self.errors("about.html", self.page(navigation=navigation)))

    def test_print_and_error_pages_do_not_need_current_navigation(self):
        for label in ("404.html", "pdfs/before-you-leave.html"):
            with self.subTest(page=label):
                self.assertEqual(self.errors(label, self.page(navigation="")), [])

    def test_poster_needs_heading_and_disclaimer_but_no_main_or_navigation(self):
        self.assertEqual(self.errors("pdfs/trifold.html",
                                     self.page(container="section", navigation="")), [])
        for headings, disclaimer, expected in (
            ("", DISCLAIMER, "expected one h1"),
            ("<h1>Poster</h1>", "", "expected one shared disclaimer"),
        ):
            with self.subTest(expected=expected):
                self.assertIn(f"pdfs/trifold.html: {expected}",
                              self.errors("pdfs/trifold.html", self.page(
                                  container="section", headings=headings,
                                  disclaimer=disclaimer, navigation="")))

    def test_redirects_keep_their_minimal_layout(self):
        for label in ("activities.html", "pdfs.html"):
            with self.subTest(page=label):
                self.assertEqual(self.errors(label, '<p><a href="checklists.html">Plan</a></p>'), [])


if __name__ == "__main__":
    unittest.main()
