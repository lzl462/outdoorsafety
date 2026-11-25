#!/usr/bin/env python3
"""Check the static site's local links, assets and core document contracts."""
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import re

ROOT = Path(__file__).resolve().parents[1]
SITE_PREFIX = "/outdoorsafety/"

class Document(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.ids, self.references, self.current = [], [], 0
        self.h1, self.main = 0, 0
        self.fields, self.equipment = 0, 0
        self.text = []
        self.feed(path.read_text(encoding="utf-8"))
    def handle_starttag(self, tag, attributes):
        a = dict(attributes)
        if "id" in a:
            self.ids.append(a["id"])
        if tag == "h1":
            self.h1 += 1
        if tag == "main":
            self.main += 1
        if tag == "dt":
            self.fields += 1
        if tag == "span" and a.get("class") == "checkbox":
            self.equipment += 1
        if a.get("aria-current") == "page":
            self.current += 1
        for key in ("href", "src"):
            if a.get(key):
                self.references.append(a[key])
        if tag == "img":
            if "alt" not in a:
                raise ValueError("Image without alt text")
            for source in a.get("srcset", "").split(","):
                if source.strip():
                    self.references.append(source.strip().split()[0])
    def handle_data(self, text):
        self.text.append(text)

def resolve(source, reference):
    url = urlsplit(reference)
    if url.scheme or url.netloc:
        return None, ""
    path = unquote(url.path)
    if path.startswith(SITE_PREFIX):
        target = ROOT / path[len(SITE_PREFIX):]
    elif path.startswith("/"):
        target = ROOT / path.lstrip("/")
    else:
        target = source.parent / path if path else source
    if target.is_dir():
        target /= "index.html"
    return target.resolve(), unquote(url.fragment)

def main():
    errors, checked = [], 0
    public = list(ROOT.glob("*.html")) + list((ROOT / "pdfs").glob("*.html"))
    docs = {}
    for path in public:
        try:
            docs[path.resolve()] = Document(path)
        except (ValueError, UnicodeError) as exc:
            errors.append(f"{path.relative_to(ROOT)}: {exc}")
    def document(path):
        if path not in docs:
            docs[path] = Document(path)
        return docs[path]
    disclaimer = "This is not an official rescue site. In an emergency, call 9-1-1."
    for path in public:
        doc = docs.get(path.resolve())
        if not doc:
            continue
        label = str(path.relative_to(ROOT))
        if any(n > 1 for n in Counter(doc.ids).values()):
            errors.append(f"{label}: duplicate IDs")
        # Redirects and the trifold have their own document layouts.
        if doc.main:
            if doc.main != 1 or doc.h1 != 1:
                errors.append(f"{label}: expected one main and one h1")
            if " ".join(" ".join(doc.text).split()).count(disclaimer) != 1:
                errors.append(f"{label}: expected one shared disclaimer")
        if path.name not in ("404.html",) and path.parent == ROOT and doc.main:
            if doc.current != 1:
                errors.append(f"{label}: expected one current page in full navigation")
        for reference in doc.references:
            if reference.startswith("tel:") and not re.fullmatch(r"tel:\+?[0-9*]+", reference):
                errors.append(f"{label}: malformed telephone link {reference}")
            target, anchor = resolve(path, reference)
            if target is None:
                continue
            checked += 1
            if not target.is_file():
                errors.append(f"{label}: missing destination {reference}")
            elif anchor and target.suffix == ".html" and anchor not in document(target).ids:
                errors.append(f"{label}: missing anchor {reference}")
    required = {
        "if.html": ["lost", "hurt", "avalanche", "water", "waiting-for-help"],
        "no-service.html": ["need-help", "before-no-signal"],
        "pack-lists.html": ["essentials", "hiking", "biking", "climbing", "winter"],
        "about.html": ["hiker-story", "rider-story", "interviews", "sources"],
    }
    for name, anchors in required.items():
        if not set(anchors).issubset(document(ROOT / name).ids):
            errors.append(f"{name}: missing established section")
    plan = document(ROOT / "pdfs/before-you-leave.html")
    if (plan.fields, plan.equipment) != (13, 8):
        errors.append("Printable plan must retain 13 fields and eight equipment lines")
    quote = "Don't go beyond your means (be honest) and make/leave a solid trip plan."
    if quote not in " ".join(" ".join(document(ROOT / "index.html").text).split()):
        errors.append("Home must retain Christine's exact quotation")
    for css in ROOT.glob("*.css"):
        for reference in re.findall(r"url\([\"']?([^\"')]+)", css.read_text()):
            target, _ = resolve(css, reference)
            if target is not None and not target.is_file():
                errors.append(f"{css.name}: missing asset {reference}")
    if errors:
        raise SystemExit("\n".join(errors))
    print(f"Checked {len(public)} public HTML files and {checked} local references; all passed.")

if __name__ == "__main__":
    main()
