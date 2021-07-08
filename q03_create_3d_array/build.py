# Default Imports
import numpy as np

# Enter solution here
def create_3d_array():
    N = 3 * 3 * 3
    arr = np.arange(start=0, stop=N, step=1)
    new_arr = np.reshape(arr, (3,3,3))
    return new_arr
create_3d_array()
