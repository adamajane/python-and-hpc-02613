import os
import sys
from time import perf_counter

import blosc
import numpy as np


def write_numpy(arr, file_name):
    np.save(f"{file_name}.npy", arr)
    os.sync()


def write_blosc(arr, file_name, cname="lz4"):
    b_arr = blosc.pack_array(arr, cname=cname)
    with open(f"{file_name}.bl", "wb") as w:
        w.write(b_arr)
    os.sync()


def read_numpy(file_name):
    return np.load(f"{file_name}.npy")


def read_blosc(file_name):
    with open(f"{file_name}.bl", "rb") as r:
        b_arr = r.read()
    return blosc.unpack_array(b_arr)


def time_op(fn, *args, **kwargs):
    t0 = perf_counter()
    fn(*args, **kwargs)
    return perf_counter() - t0


if __name__ == "__main__":
    n = int(sys.argv[1])
    arr = np.zeros((n, n, n), dtype="uint8")

    base = f"arr_{n}"
    t_wn = time_op(write_numpy, arr, base)
    t_wb = time_op(write_blosc, arr, base)
    t_rn = time_op(read_numpy, base)
    t_rb = time_op(read_blosc, base)

    print(f"{t_wn} {t_wb} {t_rn} {t_rb}")
