"""4x4 HSV grid color delta check comparing a reference image against a render.

Usage:
    python scripts/color_check.py <reference.png> <render.png>

Both images should share the same aspect ratio (resized to 256x144 by default).
A negative saturation delta means the render is greyer than the reference.
Requires: Pillow, NumPy (`pip install pillow numpy`).
"""

import sys
import numpy as np
from PIL import Image


def cells(path, grid=4):
    img = Image.open(path).convert("RGB").resize((256, 144)).convert("HSV")
    hsv = np.asarray(img).astype(float) / 255.0
    h, w = hsv.shape[:2]
    out = []
    for y in range(grid):
        for x in range(grid):
            c = hsv[y * h // grid:(y + 1) * h // grid, x * w // grid:(x + 1) * w // grid]
            out.append((c[..., 1].mean(), c[..., 2].mean()))
    return np.array(out)


def main():
    if len(sys.argv) != 3:
        print("Usage: python color_check.py <reference.png> <render.png>", file=sys.stderr)
        sys.exit(1)

    d = cells(sys.argv[2]) - cells(sys.argv[1])
    for name, col in (("saturation", 0), ("brightness", 1)):
        worst = d[np.abs(d[:, col]).argmax(), col]
        print(f"{name}: mean delta {d[:, col].mean():+.3f}, worst cell {worst:+.3f}")


if __name__ == "__main__":
    main()
