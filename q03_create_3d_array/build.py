# %load q03_create_3d_array/build.py
# Default Imports
import numpy as np

# Enter solution here
def create_3d_array():
    N = 3 ** 3
    arr = np.arange(0,N).reshape((3,3,3))
    return arr


