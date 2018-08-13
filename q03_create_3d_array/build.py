# Default Imports
import numpy as np

# Enter solution here
def create_3d_array():
    N = 3 * 3 * 3
    arr = np.arange(N)
    return np.reshape(arr, (3, 3, 3))
