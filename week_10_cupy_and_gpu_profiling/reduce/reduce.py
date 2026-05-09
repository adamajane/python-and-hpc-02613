import sys

import numpy as np
from numba import cuda, float32

TPB = 128


@cuda.jit
def reduce_kernel(data, out, n):
    s_data = cuda.shared.array(TPB, dtype=float32)
    tid = cuda.threadIdx.x
    i = cuda.grid(1)

    s_data[tid] = data[i] if i < n else float32(0.0)
    cuda.syncthreads()

    s = cuda.blockDim.x // 2
    while s > 0:
        if tid < s:
            s_data[tid] += s_data[tid + s]
        cuda.syncthreads()
        s //= 2

    if tid == 0:
        out[cuda.blockIdx.x] = s_data[0]


def get_grid(n, tpb):
    return (n + (tpb - 1)) // tpb


def reduce(x):
    x = cuda.to_device(x)
    n = x.size
    bpg = get_grid(n, TPB)
    out = cuda.device_array(bpg, dtype=x.dtype)
    while bpg > 1:
        reduce_kernel[bpg, TPB](x, out, n)
        n = bpg
        bpg = get_grid(n, TPB)
        x[:n] = out[:n]
    reduce_kernel[bpg, TPB](x, out, n)
    return out.copy_to_host()[0]


if __name__ == "__main__":
    n = int(sys.argv[1])
    x = np.random.rand(n).astype(np.float32)
    s = reduce(x)
    print(s)
