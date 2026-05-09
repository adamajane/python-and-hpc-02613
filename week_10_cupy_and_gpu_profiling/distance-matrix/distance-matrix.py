import sys

import cupy as cp
import numpy as np


def distance_matrix_oneloop(p1, p2):
    p1 = cp.radians(p1)
    p2 = cp.radians(p2)
    cos_p2_lat = cp.cos(p2[:, 0])
    D = cp.empty((len(p1), len(p2)))
    for i in range(len(p1)):
        dsin2 = cp.sin(0.5 * (p1[i] - p2)) ** 2
        cosprod = cp.cos(p1[i, 0]) * cos_p2_lat
        a = dsin2[:, 0] + cosprod * dsin2[:, 1]
        D[i, :] = 2 * cp.arcsin(cp.sqrt(a))
    D *= 6371
    return D


def distance_matrix_noloop(p1, p2):
    p1 = cp.radians(p1)
    p2 = cp.radians(p2)
    dsin2 = cp.sin(0.5 * (p1[:, None, :] - p2[None, :, :])) ** 2
    cosprod = cp.cos(p1[:, None, 0]) * cp.cos(p2[None, :, 0])
    D = 2 * cp.arcsin(cp.sqrt(dsin2[:, :, 0] + cosprod * dsin2[:, :, 1]))
    D *= 6371
    return D


def load_points(fname):
    data = np.loadtxt(fname, delimiter=",", skiprows=1, usecols=(1, 2))
    return cp.asarray(data)


def distance_stats(D):
    n = D.shape[0]
    idx = cp.triu_indices(n, k=1)
    distances = D[idx]
    return {
        "mean": float(distances.mean()),
        "std": float(distances.std()),
        "max": float(distances.max()),
        "min": float(distances.min()),
    }


if __name__ == "__main__":
    fname = sys.argv[1]
    impl = sys.argv[2] if len(sys.argv) > 2 else "noloop"

    points = load_points(fname)
    if impl == "oneloop":
        D = distance_matrix_oneloop(points, points)
    else:
        D = distance_matrix_noloop(points, points)
    cp.cuda.Stream.null.synchronize()
    print(distance_stats(D))
