import numpy as np


def outer(n, m):
    result = np.zeros((len(n), len(m)))

    for i in range(len(n)):
        for j in range(len(m)):
            result[i][j] = n[i] * m[j]

    return result
