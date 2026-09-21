#!/usr/bin/env python3
"""Build the poster (cover) images for the AI Priors record slides.

The recordings in ../AI Priors/Records are read-only source material and are
never modified. Their video content is embedded in the deck, but the *static*
cover shown on the slide (and therefore in the PDF export and the PNG previews)
is a generated navy card with the record title and a play marker — no frame of
the recording is reproduced, so no clinical content from the screen capture is
exposed in the static artefacts. The recording itself plays only when the deck
is opened in PowerPoint.

Usage:
    pip install pillow
    python3 prepare_record_posters.py
"""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
TARGET_DIR = HERE / "assets" / "record-posters"

SIZE = (1920, 1080)
NAVY = (0x0B, 0x25, 0x45, 255)
NAVY_SOFT = (0x1B, 0x3A, 0x5C, 255)
TEAL = (0x0E, 0x8C, 0x8B, 255)
TEAL_LIGHT = (0xE6, 0xF3, 0xF3, 255)
WHITE = (0xFF, 0xFF, 0xFF, 255)

POSTERS = [
    ("old-flow.png", "OLD FLOW", "Manual review of prior reports",
     "Screen recording \u00b7 01:30"),
    ("new-flow.png", "NEW FLOW", "AI patient history summary in the workflow",
     "Screen recording \u00b7 00:54"),
]

FONT_CANDIDATES = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
]


def font(size, bold=True):
    for path in FONT_CANDIDATES if bold else reversed(FONT_CANDIDATES):
        if Path(path).exists():
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def build(name, eyebrow, title, footnote):
    image = Image.new("RGBA", SIZE, NAVY)
    draw = ImageDraw.Draw(image)

    draw.rectangle([0, 0, SIZE[0], 12], fill=TEAL)
    draw.rectangle([120, 250, 1800, 830], outline=NAVY_SOFT, width=3)

    cx, cy, r = 960, 470, 90
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=TEAL, width=6)
    draw.polygon([(cx - 26, cy - 40), (cx - 26, cy + 40), (cx + 44, cy)],
                 fill=TEAL)

    draw.text((cx, 650), eyebrow, font=font(46), fill=TEAL, anchor="mm")
    draw.text((cx, 730), title, font=font(54), fill=WHITE, anchor="mm")
    draw.text((cx, 940), footnote, font=font(34, bold=False),
              fill=TEAL_LIGHT, anchor="mm")

    TARGET_DIR.mkdir(parents=True, exist_ok=True)
    image.convert("RGB").save(TARGET_DIR / name)
    print(f"Wrote {TARGET_DIR / name}")


def main():
    for args in POSTERS:
        build(*args)


if __name__ == "__main__":
    main()
