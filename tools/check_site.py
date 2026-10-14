#!/usr/bin/env python3
"""Dependency-free structural checker for static HTML repositories.

Checks local structure only; it does not make network requests.
Exit status: 0 when no errors are found, 1 otherwise.
"""
from __future__ import annotations

from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
SKIP_DIRS = {".git", ".github", "node_modules", "vendor", "dist", "build", "coverage"}
ERRORS: list[str] = []
WARNINGS: list[str] = []


class PageParser(HTMLParser):
    def __init__(self, path: Path):
        super().__init__(convert_charrefs=True)
        self.path = path
        self.ids: list[str] = []
        self.links: list[tuple[str, int]] = []
        self.images: list[tuple[dict[str, str | None], int]] = []
        self.title_seen = False
        self.in_title = False
        self.title_text = ""
        self.html_seen = False
        self.main_count = 0
        self.main_seen = False
        self.landmarks: set[str] = set()
        self.line = 1

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        if tag == "html":
            self.html_seen = True
        if tag == "title":
            self.in_title = True
            self.title_seen = True
        if tag == "main":
            self.main_count += 1
            self.main_seen = True
            self.landmarks.add("main")
        if tag == "nav":
            self.landmarks.add("nav")
        if tag == "header":
            self.landmarks.add("header")
        if tag == "footer":
            self.landmarks.add("footer")
        if attrs_dict.get("id"):
            self.ids.append(str(attrs_dict["id"]))
        if tag == "a":
            self.links.append((str(attrs_dict.get("href") or ""), self.getpos()[0]))
        if tag in {"img", "area", "input"} and tag == "img":
            self.images.append((attrs_dict, self.getpos()[0]))

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False

    def handle_data(self, data):
        if self.in_title:
            self.title_text += data.strip()

def skip(path: Path) -> bool:
    return any(part in SKIP_DIRS for part in path.parts)

html_files = sorted(
    p for p in ROOT.rglob("*.html")
    if not skip(p.relative_to(ROOT))
)

if not html_files:
    print("ERROR: No HTML files found in repository root/tree.")
    sys.exit(1)

for path in html_files:
    rel = path.relative_to(ROOT)
    try:
        source = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        ERRORS.append(f"{rel}: cannot decode as UTF-8")
        continue

    parser = PageParser(path)
    try:
        parser.feed(source)
        parser.close()
    except Exception as exc:
        ERRORS.append(f"{rel}: HTML parser error: {exc}")
        continue

    counts = Counter(parser.ids)
    duplicates = sorted(k for k, v in counts.items() if v > 1)
    for item in duplicates:
        ERRORS.append(f"{rel}: duplicate id={item!r}")

    if not parser.html_seen:
        WARNINGS.append(f"{rel}: missing <html> element")
    if not parser.title_seen or not parser.title_text.strip():
        ERRORS.append(f"{rel}: missing or empty <title>")
    if parser.main_count > 1:
        ERRORS.append(f"{rel}: {parser.main_count} <main> landmarks found; use one main landmark")
    if not parser.main_seen:
        WARNINGS.append(f"{rel}: no <main> landmark found")

    id_set = set(parser.ids)
    for href, line in parser.links:
        href = href.strip()
        if not href or href == "#":
            ERRORS.append(f"{rel}:{line}: empty or placeholder href")
        elif href.startswith("#") and len(href) > 1 and href[1:] not in id_set:
            ERRORS.append(f"{rel}:{line}: fragment target {href!r} does not exist")

    for attrs, line in parser.images:
        if "alt" not in attrs:
            ERRORS.append(f"{rel}:{line}: <img> is missing alt attribute (use alt=\"\" for decorative images)")

print(f"Scanned {len(html_files)} HTML file(s) in {ROOT}")
for warning in WARNINGS:
    print(f"WARNING: {warning}")
for error in ERRORS:
    print(f"ERROR: {error}")
if ERRORS:
    print(f"FAILED: {len(ERRORS)} error(s), {len(WARNINGS)} warning(s)")
    sys.exit(1)
print(f"PASSED: no structural errors found ({len(WARNINGS)} warning(s))")
