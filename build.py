#!/usr/bin/env python3
"""Build the deployable site into dist/.

index.html is written as a page fragment (title, links and style first, then
the body content), which is how the claude.ai preview expects it. A real web
host needs a full document, so this script wraps it and copies the images.

Usage:  python3 build.py
"""
import re
import shutil
from pathlib import Path

# Site address, e.g. "https://medipick.netlify.app" or later "https://medipick.kr".
# Used for the link preview image in KakaoTalk/Slack. Leave empty until you know it.
DOMAIN = "https://kimjoonnnn.github.io/medipick"
ROOT = Path(__file__).resolve().parent
DIST = ROOT / "dist"

src = (ROOT / "index.html").read_text(encoding="utf-8")

# Everything up to the end of the first <style> block belongs in <head>.
split = src.index("</style>") + len("</style>")
head, body = src[:split], src[split:]

# The preview-only viewport hint is not needed on a real site.
head = re.sub(r'<meta name="claude:viewport-fit-sides"[^>]*>\n?', "", head)

title = re.search(r"<title>(.*?)</title>", head).group(1)
desc_m = re.search(r'<meta name="description" content="([^"]*)"', head)
desc = desc_m.group(1) if desc_m else ""

og = f"""<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">"""
if DOMAIN:
    og += f"""
<meta property="og:url" content="{DOMAIN}/">
<meta property="og:image" content="{DOMAIN}/img/derm-lobby.jpg">"""
og += """
<meta name="theme-color" content="#FFFFFF">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='8' fill='%231E5BD6'/%3E%3Ccircle cx='16' cy='16' r='6' fill='white'/%3E%3C/svg%3E">"""

doc = f"""<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
{head.strip()}
{og}
<style>body {{ margin: 0; }} [hidden] {{ display: none !important; }}</style>
</head>
<body>
{body.strip()}
</body>
</html>
"""

if DIST.exists():
    shutil.rmtree(DIST)
(DIST / "img").mkdir(parents=True)
(DIST / "index.html").write_text(doc, encoding="utf-8")
for img in (ROOT / "img").iterdir():
    if img.suffix.lower() in {".jpg", ".jpeg", ".png", ".webp", ".svg"}:
        shutil.copy2(img, DIST / "img" / img.name)

key_set = re.search(r"var FORM_KEY = '([^']+)'", src)
print(f"Built {DIST}/index.html")
if not key_set:
    print("Note: FORM_KEY is empty, so the inquiry form will not send yet (see DEPLOY.md, step 1).")
