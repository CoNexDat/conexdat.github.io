#!/usr/bin/env python3
"""Backfill `abstract = {…}` for conexdat.bib entries that have an arXiv id.

Uses the arXiv export API (http://export.arxiv.org/api/query?id_list=<id>);
respects their request to space requests ~3s apart. Idempotent: skips
entries that already have an abstract field.
"""

from __future__ import annotations

import re
import sys
import time
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
BIB = REPO / "_bibliography" / "conexdat.bib"

ATOM_NS = "{http://www.w3.org/2005/Atom}"
ARXIV_RE = re.compile(r"\d{4}\.\d{4,5}")
ARXIV_FROM_URL_RE = re.compile(r"(?:arxiv\.org/(?:abs|pdf)/|ARXIV\.)(\d{4}\.\d{4,5})", re.IGNORECASE)

USER_AGENT = "Mozilla/5.0 (CoNexDat-Abstracts; +https://conexdat.github.io)"


def fetch_abstract(arxiv_id: str) -> str | None:
    url = f"http://export.arxiv.org/api/query?id_list={arxiv_id}"
    print(f"  ↓ {url}")
    try:
        req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = resp.read()
    except Exception as e:
        print(f"    ✗ {e}")
        return None
    try:
        root = ET.fromstring(data)
    except ET.ParseError as e:
        print(f"    ✗ XML parse: {e}")
        return None
    entry = root.find(ATOM_NS + "entry")
    if entry is None:
        print("    ✗ no entry element")
        return None
    summary = entry.find(ATOM_NS + "summary")
    if summary is None or not summary.text:
        return None
    text = re.sub(r"\s+", " ", summary.text).strip()
    print(f"    ✓ {len(text)} chars")
    return text


# --- minimal bibtex iteration (re-used logic from fetch_pdfs.py) ---

def parse_entries(text: str):
    entries = []
    i = 0
    n = len(text)
    while i < n:
        if text[i] != "@":
            i += 1
            continue
        m = re.match(r"@(\w+)\s*\{\s*([^,\s}]+)\s*,", text[i:])
        if not m:
            i += 1
            continue
        if m.group(1).lower() in ("comment", "string", "preamble"):
            i += 1
            continue
        depth = 0
        j = text.find("{", i)
        while j < n:
            c = text[j]
            if c == "{":
                depth += 1
            elif c == "}":
                depth -= 1
                if depth == 0:
                    break
            j += 1
        if depth != 0:
            break
        end = j + 1
        block = text[i:end]
        fields = parse_fields(block[m.end():])
        entries.append({"start": i, "end": end, "block": block, "key": m.group(2), "fields": fields})
        i = end
    return entries


def parse_fields(body: str) -> dict[str, str]:
    fields = {}
    i = 0
    n = len(body)
    while i < n:
        while i < n and body[i] in " \t\r\n,":
            i += 1
        if i >= n or body[i] == "}":
            break
        m = re.match(r"([A-Za-z][A-Za-z0-9_-]*)\s*=\s*", body[i:])
        if not m:
            i += 1
            continue
        name = m.group(1).lower()
        i += m.end()
        if i >= n:
            break
        if body[i] == "{":
            depth = 0
            j = i
            while j < n:
                c = body[j]
                if c == "{":
                    depth += 1
                elif c == "}":
                    depth -= 1
                    if depth == 0:
                        break
                j += 1
            value = body[i + 1:j]
            i = j + 1
        elif body[i] == '"':
            j = i + 1
            while j < n and body[j] != '"':
                if body[j] == "\\":
                    j += 2
                else:
                    j += 1
            value = body[i + 1:j]
            i = j + 1
        else:
            m2 = re.match(r"[^,}\s]+", body[i:])
            value = m2.group(0) if m2 else ""
            i += len(value)
        fields[name] = value.strip()
    return fields


def main():
    text = BIB.read_text()
    entries = parse_entries(text)
    rewrites = []
    fetched = 0

    for ent in entries:
        f = ent["fields"]
        if "abstract" in f and f["abstract"].strip():
            continue
        eprint = f.get("eprint", "")
        arxiv_id = eprint if ARXIV_RE.fullmatch(eprint) else ""
        if not arxiv_id:
            for src in (f.get("url", ""), f.get("doi", "")):
                m = ARXIV_FROM_URL_RE.search(src)
                if m:
                    arxiv_id = m.group(1)
                    break
        if not arxiv_id:
            continue

        print(f"\n[{ent['key']}] arxiv:{arxiv_id}")
        abstract = fetch_abstract(arxiv_id)
        time.sleep(3.5)            # be nice to arXiv API
        if not abstract:
            continue
        # arXiv abstracts may contain { and } (LaTeX) which would break bibtex
        # field parsing — escape with bibtex's brace-escape convention.
        abstract = abstract.replace("\\", "\\\\")
        # Inject `abstract = {<text>}` before the closing `}` of this entry.
        block = ent["block"]
        close_idx = block.rfind("}")
        body = block[:close_idx].rstrip()
        if not body.endswith(","):
            body += ","
        new_block = body + f"\n  abstract = {{{abstract}}}\n}}"
        rewrites.append((ent["start"], ent["end"], new_block))
        fetched += 1

    for start, end, new_block in sorted(rewrites, key=lambda x: -x[0]):
        text = text[:start] + new_block + text[end:]

    BIB.write_text(text)
    print(f"\nDone. Added abstracts to {fetched} entries.")


if __name__ == "__main__":
    sys.exit(main() or 0)
