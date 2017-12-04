# Default Imports
import numpy as np

# Enter solution here
def create_3d_array():
    N = 3 ** 3
    np_arr = np.arange(N)
    np_arr = np.reshape(np_arr,(3,3,3))
    return np_arr
