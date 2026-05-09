from time import perf_counter

import numpy as np
from numba import cuda


@cuda.jit
def add_kernel(x, y, out):
    i = cuda.grid(1)
    if i < x.size:
        out[i] = x[i] + y[i]


def run(x, y):
    out = np.empty_like(x)
    tpb = 128
    bpg = (x.size + tpb - 1) // tpb
    add_kernel[bpg, tpb](x, y, out)
    cuda.synchronize()
    return out


if __name__ == "__main__":
    n = 1_000_000
    x = np.random.rand(n).astype(np.float32)
    y = np.random.rand(n).astype(np.float32)

    # Warm-up (JIT compile)
    run(x, y)

    t0 = perf_counter()
    out = run(x, y)
    t1 = perf_counter()
    print(f"add_kernel(1M floats): {(t1 - t0) * 1000:.3f} ms")
    print(f"max error: {np.max(np.abs(out - (x + y))):.3e}")
