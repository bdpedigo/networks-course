import numpy as np
from numba import jit


# @jit(nopython=True)
def sample_rdpg(P, seed):
    np.random.seed(seed)
    A = np.random.binomial(np.int64(1), P)
    A[np.arange(len(A)), np.arange(len(A))] = 0.0
    return A