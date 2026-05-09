import multiprocessing
import os
import sys

import numpy as np


XMIN, XMAX = -2, 2
YMIN, YMAX = -2, 2
MAX_ITER = 100
OUT_PATH = "mandelbrot.raw"


def mandelbrot_escape_time(c):
    z = 0
    for i in range(MAX_ITER):
        z = z**2 + c
        if abs(z) > 2.0:
            return i
    return MAX_ITER


def _compute_rows(args):
    path, n, row_start, row_end = args
    arr = np.memmap(path, dtype=np.int32, mode="r+", shape=(n, n))
    x_values = np.linspace(XMIN, XMAX, n)
    y_values = np.linspace(YMIN, YMAX, n)
    for i in range(row_start, row_end):
        x = x_values[i]
        for j, y in enumerate(y_values):
            arr[i, j] = mandelbrot_escape_time(complex(x, y))
    arr.flush()


if __name__ == "__main__":
    n = int(sys.argv[1])
    n_proc = int(sys.argv[2]) if len(sys.argv) > 2 else os.cpu_count()

    arr = np.memmap(OUT_PATH, dtype=np.int32, mode="w+", shape=(n, n))
    del arr

    rows_per = (n + n_proc - 1) // n_proc
    tasks = [
        (OUT_PATH, n, i, min(i + rows_per, n)) for i in range(0, n, rows_per)
    ]

    with multiprocessing.Pool(n_proc) as pool:
        pool.map(_compute_rows, tasks)

    print(OUT_PATH)
