# banner generator

Regenerates the README banner and section-header images: transparent
light/dark PNG pairs in the house style (Bricolage Grotesque, tokens from
[slop/house-style](https://github.com/baely/slop/tree/main/house-style)),
rendered with headless Chrome. Requires only python3 and Chrome.

```sh
cp tools/banner/banner.config.example.json banner.config.json
# edit banner.config.json with the real text
python3 tools/banner/generate.py
```

Outputs land in `assets/` (overwriting the committed images), and the
script prints the `<picture>` markup for each pair.

**`banner.config.json` is gitignored on purpose.** The point of rendering
this text as images is to keep it out of anything crawlable in this public
repo — committing the config would defeat that. Keep it local; never commit
it or paste its contents into tracked files.

Config knobs: `banner.heading` and `banner.lines` control the hero text;
each entry in `headers` becomes a `header-<slug>-{light,dark}.png` pair.
Sizes (`height`, `heading_size`, `line_size`, per-header `size`) are in 2x
pixels — images are authored at twice `display_width` and displayed at
half size for crisp text.
