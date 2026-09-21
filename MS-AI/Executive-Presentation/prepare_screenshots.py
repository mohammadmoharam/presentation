#!/usr/bin/env python3
"""Build redacted copies of the AI Dashboard screenshots for the deck.

The originals in ../AI Dashboard/Screenshots are read-only source material and
are never modified. Each copy is identical to its source except that the
personally identifiable regions listed in REDACTIONS are pixelated:

* the signed-in user chip in the top-right header of every screenshot;
* the `REQUESTED BY` email address in Screenshot_4.png.

Nothing else is cropped or altered, so aspect ratios stay unchanged.

Usage:
    pip install pillow
    python3 prepare_screenshots.py
"""

from pathlib import Path

from PIL import Image

HERE = Path(__file__).resolve().parent
SOURCE_DIR = HERE.parent / "AI Dashboard" / "Screenshots"
TARGET_DIR = HERE / "assets" / "dashboard-screenshots"

# Pixel boxes (left, top, right, bottom) redacted in each screenshot.
REDACTIONS = {
    "Screenshot_1.png": [(1620, 0, 1871, 50)],
    "Screenshot_2.png": [(1620, 0, 1893, 50)],
    "Screenshot_3.png": [(1620, 0, 1877, 56)],
    "Screenshot_4.png": [(1620, 0, 1885, 50), (408, 222, 684, 262)],
}


def pixelate(image, box, blocks=12):
    left, top, right, bottom = box
    left, top = max(left, 0), max(top, 0)
    right, bottom = min(right, image.width), min(bottom, image.height)
    if right <= left or bottom <= top:
        return
    region = image.crop((left, top, right, bottom))
    small = region.resize(
        (max(region.width // blocks, 1), max(region.height // blocks, 1)),
        Image.BILINEAR,
    )
    image.paste(small.resize(region.size, Image.NEAREST), (left, top))


def main():
    TARGET_DIR.mkdir(parents=True, exist_ok=True)
    for name, boxes in REDACTIONS.items():
        with Image.open(SOURCE_DIR / name) as src:
            image = src.convert("RGBA")
        for box in boxes:
            pixelate(image, box)
        image.save(TARGET_DIR / name)
        print(f"Wrote {TARGET_DIR / name} ({len(boxes)} redacted region(s))")


if __name__ == "__main__":
    main()
