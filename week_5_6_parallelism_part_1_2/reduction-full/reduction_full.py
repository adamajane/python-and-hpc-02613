import ctypes
import multiprocessing as mp
import sys
from time import perf_counter as time

import numpy as np
from PIL import Image


def init(shared_arr_):
    global shared_arr
    shared_arr = shared_arr_


def tonumpyarray(mp_arr):
    return np.frombuffer(mp_arr, dtype="float32")


def reduce_step(args):
    b, e, stride, offset, elemshape = args
    arr = tonumpyarray(shared_arr).reshape((-1,) + elemshape)
    arr[b:e:stride] += arr[b + offset : e + offset : stride]


if __name__ == "__main__":
    n_processes = 4
    chunk = 16

    data = np.load(sys.argv[1])
    elemshape = data.shape[1:]
    shared_arr = mp.RawArray(ctypes.c_float, data.size)
    arr = tonumpyarray(shared_arr).reshape(data.shape)
    np.copyto(arr, data)
    n = len(arr)
    del data

    t = time()
    pool = mp.Pool(n_processes, initializer=init, initargs=(shared_arr,))

    stride = 2
    while stride // 2 < n:
        offset = stride // 2
        end_source = n - offset
        block = chunk * stride
        tasks = [
            (b, min(b + block, end_source), stride, offset, elemshape)
            for b in range(0, end_source, block)
        ]
        pool.map(reduce_step, tasks, chunksize=1)
        stride *= 2

    pool.close()
    pool.join()

    print(time() - t)
    final_image = arr[0] / n
    Image.fromarray((255 * final_image.astype(float)).astype("uint8")).save(
        "result.png"
    )
