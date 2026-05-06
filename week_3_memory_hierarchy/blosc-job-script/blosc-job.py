import timeit
import numpy as np

N = 4096
REPS = 1000

mat = np.random.rand(N, N)

col_times = timeit.repeat("2 * mat[:, 0]", globals=globals(), number=REPS, repeat=5)
row_times = timeit.repeat("2 * mat[0, :]", globals=globals(), number=REPS, repeat=5)

col_best = min(col_times) / REPS
row_best = min(row_times) / REPS

print(f"Matrix shape: {mat.shape}, dtype: {mat.dtype}")
print(f"Repetitions: {REPS}")
print(f"2 * mat[:, 0]  (column): {col_best * 1e6:.2f} µs  (best of 5 runs)")
print(f"2 * mat[0, :]  (row):    {row_best * 1e6:.2f} µs  (best of 5 runs)")
print(f"Ratio col/row: {col_best / row_best:.2f}x")
