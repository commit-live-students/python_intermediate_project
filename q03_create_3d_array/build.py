# %load q03_create_3d_array/build.py
# Default Imports
import numpy as np

# Enter solution here
def create_3d_array():
    arr = np.arange(0,3**3).reshape((3,3,3))
    return arr


