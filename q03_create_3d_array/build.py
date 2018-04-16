# %load q03_create_3d_array/build.py
# Default Imports
import numpy as np

N = 27
# Enter solution here
def create_3d_array():
    arr = np.arange(0, N, dtype=np.dtype('int'))
    arr = arr.reshape((3,3,3))
    return arr
create_3d_array()


