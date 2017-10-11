# Default Imports
import numpy as np

# Enter solution here
def create_3d_array():
    d1, d2, d3 = 3, 3, 3
    N = d1 * d2 * d3
    arr = np.arange(N)
    return arr.reshape(d1, d2, d3)
