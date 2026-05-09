import timeit
import numpy as np

REPS = 1000
SIZES = np.unique(np.logspace(1, 4.5, 20).astype(int))

print(f"# size_bytes  size_kb  col_time_s  row_time_s  col_mflops  row_mflops")
for size in SIZES:
    mat = np.random.rand(size, size)
    bytes_per_vec = size * mat.dtype.itemsize

    col_times = timeit.repeat(
        "2 * mat[:, 0]", globals={"mat": mat}, number=REPS, repeat=5
    )
    row_times = timeit.repeat(
        "2 * mat[0, :]", globals={"mat": mat}, number=REPS, repeat=5
    )

    col_t = min(col_times) / REPS
    row_t = min(row_times) / REPS
    col_mflops = size / col_t / 1e6
    row_mflops = size / row_t / 1e6

    print(
        f"{bytes_per_vec:10d}  {bytes_per_vec / 1024:8.3f}  "
        f"{col_t:.3e}  {row_t:.3e}  {col_mflops:10.2f}  {row_mflops:10.2f}"
    )
