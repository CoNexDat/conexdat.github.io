#!/usr/bin/env python3
"""Fetch open-access PDFs for conexdat.bib entries and rewrite the bib in place.

For each entry that has an arXiv eprint or a URL pointing at one of the
known open-access mirrors (cnet.fi.uba.ar / hal.inria.fr / tma.ifip.org /
*.jaiio.org.ar / eccs2012.eu / rfc-editor.org), download the PDF into
assets/pdf/<year>_<venue>_<firstauthor>.pdf and add a `pdf = {<basename>}`
line to that entry. Idempotent: skips entries that already have `pdf=` set
or whose target file already exists.

Run from the repo root:
    python3 _scripts/fetch_pdfs.py
"""

from __future__ import annotations

import os
import re
import sys
import time
import unicodedata
import urllib.request
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
BIB = REPO / "_bibliography" / "conexdat.bib"
PDF_DIR = REPO / "assets" / "pdf"
PDF_DIR.mkdir(parents=True, exist_ok=True)

USER_AGENT = "Mozilla/5.0 (CoNexDat-PDF-Mirror; +https://conexdat.github.io)"

# URL patterns considered safe to mirror (author-hosted / open access).
OPEN_HOST_RE = re.compile(
    r"^(https?://("
    r"cnet\.fi\.uba\.ar/.*\.pdf"
    r"|hal\.inria\.fr/docs/.*\.pdf"
    r"|tma\.ifip\.org/.*\.pdf"
    r"|www\.\d+jaiio\.org\.ar/.*\.pdf"
    r"|eccs\d+\.eu/media/.*\.pdf"
    r"|www\.rfc-editor\.org/rfc/.*\.pdf"
    r"))$",
    re.IGNORECASE,
)

ARXIV_RE = re.compile(r"^\d{4}\.\d{4,5}$")


def slug(text: str, maxlen: int = 30) -> str:
    """Lowercase, ASCII-only, non-alnum collapsed to single underscore."""
    if not text:
        return "misc"
    nfkd = unicodedata.normalize("NFKD", text)
    ascii_only = nfkd.encode("ascii", "ignore").decode("ascii")
    cleaned = re.sub(r"[^a-zA-Z0-9]+", "-", ascii_only).strip("-").lower()
    return cleaned[:maxlen] or "misc"


def _detex(s: str) -> str:
    """Strip common bibtex/TeX accent commands and brace groups, leaving the
    accented letter intact."""
    if not s:
        return s
    # {\'o}, \'{o}, \'o, \"o, \^o, \~o, \=o, \.o, \`o → o
    s = re.sub(r"\{\\[`'\"^~=.]\{?([A-Za-z])\}?\}", r"\1", s)
    s = re.sub(r"\\[`'\"^~=.]\{?([A-Za-z])\}?", r"\1", s)
    # Special chars: {\ss}, {\o}, {\aa}, {\l}, etc → letter
    s = re.sub(r"\{\\(ss|o|aa|ae|oe|l|i|j)\}", r"\1", s)
    # Drop remaining braces / backslashes
    s = re.sub(r"[{}\\]", "", s)
    return s


def first_author_lastname(author_field: str) -> str:
    """Extract a slug from the first author in a bibtex `author = {...}` value."""
    if not author_field:
        return "anon"
    # Authors are separated by " and ".
    first = re.split(r"\s+and\s+", author_field, maxsplit=1)[0].strip()
    first = _detex(first)
    # Two formats: "Last, First" or "First Last".
    if "," in first:
        last = first.split(",", 1)[0].strip()
    else:
        tokens = first.split()
        # Last token is usually the surname — but if there are 3+ tokens with
        # no comma, the bib entry is probably mis-formatted (e.g. missing
        # comma after a hispanic surname). Take the *first* token in that
        # case as a best-effort fallback.
        if len(tokens) >= 3:
            last = tokens[0]
        elif tokens:
            last = tokens[-1]
        else:
            last = first
    return slug(last, 20)


def parse_entries(text: str):
    """Yield (start_offset, end_offset, raw_block, type, key, fields) for each entry.

    Returns a list to allow in-place rewriting by offset (in reverse order).
    """
    entries = []
    i = 0
    n = len(text)
    while i < n:
        if text[i] != "@":
            i += 1
            continue
        # Match "@type{"
        m = re.match(r"@(\w+)\s*\{\s*([^,\s}]+)\s*,", text[i:])
        if not m:
            i += 1
            continue
        entry_type = m.group(1).lower()
        if entry_type in ("comment", "string", "preamble"):
            i += 1
            continue
        key = m.group(2)
        # Walk balanced braces from the opening brace after @type
        brace_open = text.find("{", i)
        depth = 0
        j = brace_open
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
            break  # malformed; bail
        end = j + 1
        block = text[i:end]
        fields = parse_fields(block[m.end():])  # everything after `@type{key,`
        entries.append({
            "start": i,
            "end": end,
            "block": block,
            "type": entry_type,
            "key": key,
            "fields": fields,
        })
        i = end
    return entries


def parse_fields(body: str) -> dict[str, str]:
    """Parse `key = {value}` or `key = "value"` pairs from an entry body.

    The body is everything between `@type{key,` and the final `}` of the entry.
    """
    fields = {}
    i = 0
    n = len(body)
    while i < n:
        # Skip whitespace and commas
        while i < n and body[i] in " \t\r\n,":
            i += 1
        if i >= n or body[i] == "}":
            break
        # Read field name
        m = re.match(r"([A-Za-z][A-Za-z0-9_-]*)\s*=\s*", body[i:])
        if not m:
            i += 1
            continue
        name = m.group(1).lower()
        i += m.end()
        # Read value: braced, quoted, or bare-number
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


def venue_slug(fields: dict[str, str]) -> str:
    venue = (
        fields.get("journal")
        or fields.get("booktitle")
        or fields.get("series")
        or fields.get("howpublished")
        or fields.get("school")
        or "misc"
    )
    venue = re.sub(r"\\[a-zA-Z]+", "", venue)         # drop \LaTeX commands
    venue = re.sub(r"\{|\}", "", venue)
    venue = venue.split(",")[0].split("(")[0]         # short head
    return slug(venue, 22)


def target_basename(fields: dict[str, str], for_arxiv: bool = False) -> str:
    year = re.sub(r"\D", "", fields.get("year", "")) or "xxxx"
    author = first_author_lastname(fields.get("author", ""))
    venue = "arxiv" if for_arxiv else venue_slug(fields)
    return f"{year}_{venue}_{author}.pdf"


def download(url: str, dest: Path) -> bool:
    print(f"  ↓ {url}")
    try:
        req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = resp.read()
        if not data.startswith(b"%PDF") and len(data) < 1024:
            print(f"    ! looks empty / not PDF ({len(data)} bytes); skipping")
            return False
        dest.write_bytes(data)
        print(f"    ✓ {dest.name} ({len(data)//1024} KB)")
        return True
    except Exception as e:
        print(f"    ✗ {e}")
        return False


def main():
    text = BIB.read_text()
    entries = parse_entries(text)
    print(f"Parsed {len(entries)} entries")

    # Replacements: (start_of_block_to_modify, end, new_block_text)
    rewrites = []
    downloaded = 0

    for ent in entries:
        f = ent["fields"]
        if "pdf" in f:
            continue  # already has a local PDF link

        url = f.get("url", "").strip()
        eprint = f.get("eprint", "").strip()
        archive = f.get("archiveprefix", "").strip().lower()

        download_url = None
        for_arxiv = False
        # Also detect arXiv ids in url= or doi= when no explicit eprint field.
        arxiv_id = eprint if (eprint and ARXIV_RE.match(eprint)) else ""
        if not arxiv_id:
            for src in (url, f.get("doi", "")):
                m = re.search(r"(?:arxiv\.org/(?:abs|pdf)/|ARXIV\.)(\d{4}\.\d{4,5})", src or "", re.IGNORECASE)
                if m:
                    arxiv_id = m.group(1)
                    break
        if arxiv_id:
            download_url = f"https://arxiv.org/pdf/{arxiv_id}.pdf"
            for_arxiv = True
        elif url and OPEN_HOST_RE.match(url):
            download_url = url
        else:
            continue

        basename = target_basename(f, for_arxiv=for_arxiv)
        # Disambiguate collisions
        dest = PDF_DIR / basename
        suffix = 1
        while dest.exists() and suffix < 10:
            stem = basename[:-4]
            dest = PDF_DIR / f"{stem}_{suffix}.pdf"
            suffix += 1
        if dest.exists():
            print(f"  · {ent['key']}: target {basename} already exists, skipping fetch")
        else:
            print(f"\n[{ent['key']}] → {dest.name}")
            ok = download(download_url, dest)
            if not ok:
                continue
            time.sleep(0.4)
            downloaded += 1

        # Inject `pdf = {<basename>},` before the closing `}` of this entry.
        block = ent["block"]
        # Find the last `}` and back up past trailing whitespace/comma.
        close_idx = block.rfind("}")
        if close_idx == -1:
            continue
        body = block[:close_idx].rstrip()
        if not body.endswith(","):
            body += ","
        new_block = body + f"\n  pdf = {{{dest.name}}}\n}}"
        rewrites.append((ent["start"], ent["end"], new_block))

    # Apply rewrites in reverse offset order so earlier offsets stay valid.
    for start, end, new_block in sorted(rewrites, key=lambda x: -x[0]):
        text = text[:start] + new_block + text[end:]

    BIB.write_text(text)
    print(f"\nDone. Downloaded {downloaded} PDFs, updated {len(rewrites)} entries.")


if __name__ == "__main__":
    sys.exit(main() or 0)
