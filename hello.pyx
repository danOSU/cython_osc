from cython.parallel cimport prange
cimport cython
from libc.math cimport sin

import numpy as np

@cython.boundscheck(False)
@cython.wraparound(False)
def do_sine(double[:,:,:,:,:] input):
    cdef double[:,:,:,:,:] output = np.empty_like(input)
    cdef Py_ssize_t i, j, k, l, m

    for i in prange(input.shape[0], nogil=True):
        for j in range(input.shape[1]):
            for k in range(input.shape[2]):
                for l in range(input.shape[3]):
                    for m in range(input.shape[4]):
                        output[i, j, k, l, m] = sin(input[i, j, k, l, m])
    return np.asarray(output)


