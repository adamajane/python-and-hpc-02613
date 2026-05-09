import sys
import multiprocessing
from time import perf_counter

import numpy as np


def mandelbrot_escape_time(c):
    z = 0
    for i in range(100):
        z = z**2 + c
        if np.abs(z) > 2.0:
            return i
    return 100


def _compute_chunk(points_chunk):
    return np.array([mandelbrot_escape_time(c) for c in points_chunk])


def generate_mandelbrot_set_chunks(points, num_processes, chunk_size=1000):
    chunks = [points[i : i + chunk_size] for i in range(0, len(points), chunk_size)]
    with multiprocessing.Pool(num_processes) as pool:
        results = pool.map(_compute_chunk, chunks)
    return np.concatenate(results)


if __name__ == "__main__":
    num_proc = int(sys.argv[1]) if len(sys.argv) > 1 else 1

    width = 800
    height = 800
    x_values = np.linspace(-2, 2, width)
    y_values = np.linspace(-2, 2, height)
    points = np.array([complex(x, y) for x in x_values for y in y_values])

    t0 = perf_counter()
    escape_times = generate_mandelbrot_set_chunks(points, num_proc)
    t1 = perf_counter()

    print(f"num_proc={num_proc} time={t1 - t0:.4f}s")
