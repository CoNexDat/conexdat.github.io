#!/usr/bin/env python3
"""Homogenise journal / booktitle / series field values in conexdat.bib.

Apply a small replacement map (canonical names, expanded abbreviations,
typo fixes), trim trailing whitespace inside the braces, and report a diff
summary. Operates in place — re-runnable, idempotent.
"""

from __future__ import annotations

import re
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
BIB = REPO / "_bibliography" / "conexdat.bib"

# Exact-match replacements applied to the contents of journal/booktitle/series
# field braces (case-sensitive). Keep this list short and well-curated.
REPLACEMENTS = {
    # Journal abbreviations → full names
    "arXiv e-print":                          "arXiv",
    "arXiv preprint":                         "arXiv",
    "CoRR":                                   "arXiv",
    "Sci. Rep.":                              "Scientific Reports",
    "Phys. Rev. E":                           "Physical Review E",
    "New J. Phys":                            "New Journal of Physics",
    "New J. Phys.":                           "New Journal of Physics",
    "Theor. Comput. Sci.":                    "Theoretical Computer Science",
    "SIGCOMM Comput. Commun. Rev.":           "ACM SIGCOMM Computer Communication Review",
    # Spanish/French typo fixes
    "Congreso de Microelectr\\'ocnica Aplicada 2010":
        "Congreso de Microelectr\\'onica Aplicada 2010",
    # Booktitle: strip the dangling "<hal-01134295" comment seen in one entry.
    "Fourth conference on the Analysis of Mobile Phone Datasets (NetMob 2015), <hal-01134295":
        "Fourth Conference on the Analysis of Mobile Phone Datasets (NetMob 2015)",
}

VENUE_FIELDS = ("journal", "booktitle", "series")

FIELD_RE = re.compile(
    r"^(\s*(?:" + "|".join(VENUE_FIELDS) + r")\s*=\s*)(\{+)([^{}]*(?:\{[^{}]*\}[^{}]*)*)(\}+)(\s*,?\s*)$",
    re.MULTILINE,
)


def normalise(value: str) -> str:
    v = value.strip()
    return REPLACEMENTS.get(v, v)


def main():
    text = BIB.read_text()
    changes = []

    def repl(m):
        prefix, opens, value, closes, suffix = m.group(1), m.group(2), m.group(3), m.group(4), m.group(5)
        new_value = normalise(value)
        # Preserve the brace nesting (single vs double braces) — bibtex uses
        # double braces for capitalisation preservation, don't disturb it.
        if new_value != value.strip() or value != value.strip():
            changes.append((value.strip(), new_value))
        return f"{prefix}{opens}{new_value}{closes}{suffix}"

    new_text = FIELD_RE.sub(repl, text)

    if new_text != text:
        BIB.write_text(new_text)
        print(f"Updated {len(changes)} venue values:")
        for old, new in sorted(set(changes)):
            if old != new:
                print(f"  · {old!r} → {new!r}")
            else:
                print(f"  · trimmed whitespace: {old!r}")
    else:
        print("No changes (already normalised).")


if __name__ == "__main__":
    main()
