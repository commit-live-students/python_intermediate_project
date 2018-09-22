# %load q03_create_3d_array/build.py
# Default Imports
import numpy as np

# Enter solution here
def create_3d_array():
    n = 27
    arr = np.array(range(n))
    return arr.reshape((3,3,3))

