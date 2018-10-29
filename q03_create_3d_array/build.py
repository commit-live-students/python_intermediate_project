# %load q03_create_3d_array/build.py
# Default Imports
import numpy as np

# Enter solution here
def create_3d_array():
    arr = np.zeros((3,3,3))
    N = arr.size
    N

    arr = np.arange(N).reshape((3,3,3))

    return arr


