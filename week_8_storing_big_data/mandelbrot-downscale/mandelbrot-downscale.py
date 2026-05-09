import sys

import numpy as np
from PIL import Image


if __name__ == "__main__":
    path = sys.argv[1]
    n = int(sys.argv[2])
    step = int(sys.argv[3])

    arr = np.memmap(path, dtype=np.int32, mode="r", shape=(n, n))
    sub = arr[::step, ::step]

    img = (sub.astype(np.float32) * (255.0 / 100.0)).clip(0, 255).astype(np.uint8)
    Image.fromarray(img).save("mandelbrot.png")
    print(f"saved mandelbrot.png shape={img.shape}")
