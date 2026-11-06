#!/usr/bin/env python3
"""Scan files for words you never want to publish (your name, client names, emails).

Usage: python3 scripts/scrub.py words.txt [paths...]
words.txt holds one term per line (case-insensitive, whole words). Paths default to the repo.
Run it before sharing a fork or a variant of your skills. Exits 1 if anything is found.
"""
import re, sys
from pathlib import Path

if len(sys.argv) < 2:
    sys.exit(__doc__)
terms = [t.strip() for t in Path(sys.argv[1]).read_text().splitlines() if t.strip() and not t.startswith("#")]
roots = [Path(p) for p in sys.argv[2:]] or [Path(__file__).resolve().parent.parent]
pat = re.compile(r"(?<![A-Za-z])(" + "|".join(re.escape(t) for t in terms) + r")(?![A-Za-z])", re.I)
found = 0
for root in roots:
    for f in ([root] if root.is_file() else root.rglob("*")):
        if f.is_file() and ".git" not in f.parts and f.suffix in {".md", ".toml", ".json", ".py", ".txt", ".html", ".yaml", ".yml"}:
            for i, line in enumerate(f.read_text(errors="ignore").splitlines(), 1):
                for m in pat.finditer(line):
                    print(f"{f}:{i}: {m.group(0)!r} in: {line.strip()[:120]}")
                    found += 1
print(f"{found} match(es)." if found else "Clean: no listed terms found.")
sys.exit(1 if found else 0)
