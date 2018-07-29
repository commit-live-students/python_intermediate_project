# %load q03_create_3d_array/build.py
# Default Imports
import numpy as np

def create_3d_array():
    arr = np.array(np.arange(27))
    arr = np.reshape(arr,(3,3,3))
    return arr



