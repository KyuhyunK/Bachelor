"""Build index.html (standalone, for GitHub Pages) from ski-trip-breakdown.html (the claude.ai artifact source).

The artifact source has no <!doctype>/<html>/<head>/<body> because the claude.ai viewer adds them.
A browser opening the file directly needs them, so this script adds a minimal document shell.
"""
from pathlib import Path

here = Path(__file__).parent
src = (here / "ski-trip-breakdown.html").read_text(encoding="utf-8")
shell = (
    '<!doctype html>\n<html lang="en">\n<meta charset="utf-8">\n'
    '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
)
(here / "index.html").write_text(shell + src + "\n</html>\n", encoding="utf-8")
print("wrote index.html")
