#!/usr/bin/env python3

import numpy as np

inputs = [1.0, 2.0, 3.0, 2.5]
weights = [
    [0.2, 0.8, -0.5, 1.0],
    [0.5, -0.91, 0.26, -0.5],
    [-0.26, -0.27, 0.17, 0.87],
]
biases = [2.0, 3.0, 0.5]

# When we add two vectors using NumPy, each i-th element is
# added together resulting in a new vector of the same size.
# This is both a simplification and an optimization
layer_outputs = np.dot(weights, inputs) + biases

print(layer_outputs)
