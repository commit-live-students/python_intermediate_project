# %load q03_create_3d_array/build.py
# Default Imports
import numpy as np

# Enter solution here
def create_3d_array():
    N = 3 * 3 * 3
    array1 = np.array(np.arange(0, N, 1))
    array2 = array1.reshape(3,3,3)
    array2
    return array2



