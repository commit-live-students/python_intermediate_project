# Default Imports
import numpy as np

# Enter solution here
def create_3d_array():
    N = 3 * 3 * 3
    array = np.arange(N)
    return np.reshape(array, (3, 3, 3))
