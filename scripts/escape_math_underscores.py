#!/usr/bin/env python3
"""
Bulk-fix math underscore/asterisk collisions in a Friday blog post.

USE WHEN: `grep -c "<em>" dist/hermes/<slug>/index.html` returns a non-zero
count after `npx astro build`, AND inspection of `<em>` snippets shows they
contain math fragments (e.g., `<em>{[H]} = ...$`). That means the markdown
parser ate `_..._` or `*...*` inside `$...$` math segments as italic before
MathJax got to render them.

WHAT IT DOES: Inside every inline-math `$...$` segment and display-math
`$$...$$` segment on a single line, escape unescaped `_` as `\\_` and
unescaped `*` as `\\*`. MathJax accepts both as literal subscript / literal
asterisk, so the math still renders correctly — but the markdown parser
no longer sees pairs of unescaped delimiters to wrap in <em>.

LIMITATION: Only handles single-line math segments. Multi-line display math
($$\n...\n$$) is rare for us and not handled here; if you have multi-line
display math with collisions, fix by hand.

USAGE:
    python3 scripts/escape_math_underscores.py path/to/post.md

Then rebuild and re-check:
    cd ~/clawd/friday-blog && npx astro build
    grep -c "<em>" dist/hermes/<slug>/index.html  # should be 0

Pre-existing intentional italic (e.g., the word *however* in prose) is NOT
touched because the regex only matches inside `$...$`.
"""
import re
import sys
from pathlib import Path


def fix_math(match: re.Match) -> str:
    s = match.group(0)
    s = re.sub(r"(?<!\\)_", r"\_", s)
    s = re.sub(r"(?<!\\)\*", r"\*", s)
    return s


def fix_file(path: Path) -> int:
    raw = path.read_text(encoding="utf-8")
    fixed = re.sub(r"\$[^\$\n]+\$", fix_math, raw)
    fixed = re.sub(r"\$\$[^\$\n]+\$\$", fix_math, fixed)
    if fixed == raw:
        print(f"{path}: nothing to fix")
        return 0
    path.write_text(fixed, encoding="utf-8")
    # Count how many segments we touched
    print(f"{path}: math underscores/asterisks escaped.")
    return 1


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(2)
    target = Path(sys.argv[1])
    if not target.is_file():
        print(f"error: {target} is not a file", file=sys.stderr)
        sys.exit(1)
    fix_file(target)
