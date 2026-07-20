#!/usr/bin/env python3
"""Regenerate the README banner and section-header images.

Renders transparent light/dark PNGs in the house style (slop/house-style)
using headless Chrome. No dependencies beyond python3 and Chrome.

Usage:
    python3 tools/banner/generate.py [path/to/banner.config.json]

Defaults to banner.config.json at the repo root; falls back to the example
config next to this script. The real config is gitignored on purpose: it
contains personal details as text, which this repo keeps out of anything
crawlable. Never commit it.
"""

import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
SCRIPT_DIR = Path(__file__).resolve().parent

# house-style tokens (public: baely/slop house-style/house.css)
FONTS = "https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,800&family=JetBrains+Mono:wght@400;500;700&display=swap"
THEMES = {
    "light": {"text": "#131316", "text2": "#55555e"},
    "dark": {"text": "#f2f2f4", "text2": "#a3a3ad"},
}

PAGE = """<meta charset="utf-8">
<link href="{fonts}" rel="stylesheet">
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    width: {width}px; height: {height}px; overflow: hidden; padding: 8px;
    background: transparent;
  }}
  h1 {{
    font-family: 'Bricolage Grotesque', system-ui, sans-serif;
    font-weight: 800; letter-spacing: -0.03em; line-height: 1.1;
    font-size: {heading_size}px; color: {text};
  }}
  .detail {{
    margin-top: 24px;
    font-family: 'JetBrains Mono', ui-monospace, monospace;
    font-size: {line_size}px; line-height: 1.5; color: {text2};
  }}
</style>
<h1>{heading}</h1>
{detail}
"""


def find_chrome():
    candidates = [
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Chromium.app/Contents/MacOS/Chromium",
        shutil.which("google-chrome"),
        shutil.which("chromium"),
    ]
    for c in candidates:
        if c and Path(c).exists():
            return c
    sys.exit("error: could not find a Chrome/Chromium binary")


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def render(chrome, html, width, height, out_path):
    with tempfile.TemporaryDirectory() as td:
        page = Path(td) / "page.html"
        page.write_text(html)
        subprocess.run(
            [
                chrome,
                "--headless=new",
                "--disable-gpu",
                "--hide-scrollbars",
                "--force-device-scale-factor=1",
                f"--window-size={width},{height}",
                "--default-background-color=00000000",
                "--virtual-time-budget=10000",
                f"--screenshot={out_path}",
                page.as_uri(),
            ],
            check=True,
            capture_output=True,
        )
    print(f"  wrote {out_path}")


def main():
    if len(sys.argv) > 1:
        config_path = Path(sys.argv[1])
    elif (REPO_ROOT / "banner.config.json").exists():
        config_path = REPO_ROOT / "banner.config.json"
    else:
        config_path = SCRIPT_DIR / "banner.config.example.json"
        print(f"note: no banner.config.json found, using {config_path.name}")
    cfg = json.loads(config_path.read_text())

    chrome = find_chrome()
    out_dir = REPO_ROOT / cfg.get("output_dir", "assets")
    out_dir.mkdir(exist_ok=True)
    display_width = cfg.get("display_width", 832)
    # authored at 2x the displayed size for crisp rendering
    width = display_width * 2

    banner = cfg["banner"]
    for theme, colors in THEMES.items():
        detail = ""
        if banner.get("lines"):
            detail = '<div class="detail">%s</div>' % "<br>".join(
                esc(l) for l in banner["lines"]
            )
        html = PAGE.format(
            fonts=FONTS,
            width=width,
            height=banner.get("height", 272),
            heading_size=banner.get("heading_size", 104),
            line_size=banner.get("line_size", 28),
            heading=esc(banner["heading"]),
            detail=detail,
            **colors,
        )
        render(chrome, html, width, banner.get("height", 272),
               out_dir / f"banner-{theme}.png")

    for header in cfg.get("headers", []):
        for theme, colors in THEMES.items():
            html = PAGE.format(
                fonts=FONTS,
                width=width,
                height=header.get("height", 80),
                heading_size=header.get("size", 56),
                line_size=28,
                heading=esc(header["text"]),
                detail="",
                **colors,
            )
            render(chrome, html, width, header.get("height", 80),
                   out_dir / f"header-{header['slug']}-{theme}.png")

    rel = out_dir.relative_to(REPO_ROOT)
    print("\nREADME markup (per image pair):\n")
    names = ["banner"] + [f"header-{h['slug']}" for h in cfg.get("headers", [])]
    for name in names:
        print(f"""<picture>
  <source media="(prefers-color-scheme: dark)" srcset="{rel}/{name}-dark.png">
  <img src="{rel}/{name}-light.png" alt="" width="{display_width}">
</picture>
""")


if __name__ == "__main__":
    main()
