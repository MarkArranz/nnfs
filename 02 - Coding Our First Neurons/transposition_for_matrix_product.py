#!/usr/bin/env python3

import numpy as np

a = [1, 2, 3]
b = [2, 3, 4]

# To transform a list into a matrix containing a single row shape (1, n)
# we can put it into a list and create a numpy array:
row_vector = np.array([a])
print(row_vector, row_vector.shape)

# Or we can turn it into a 1D array and expand
# dimensions using one of NumPy's abilities:
row_vector = np.expand_dims(np.array(a), axis=0)
print(row_vector, row_vector.shape)

# A column vector is a matrix where the second dimension's size equals 1
# with a shape (n, 1). With NumPy, it can be created the same way as a row
# vector, but needs to be additionally transposed:
col_vector = np.expand_dims(np.array(b), axis=1)
print(col_vector, col_vector.shape)

# Or simply:
col_vector = np.array([b]).T
print(col_vector, col_vector.shape)

# NumPy does NOT have a dedicated method for performing matrix product -
# the dot product and matrix product are both implemented in a single method: np.dot()
print(np.dot(row_vector, col_vector))
