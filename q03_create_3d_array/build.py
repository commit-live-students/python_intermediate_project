# %load q03_create_3d_array/build.py
# Default Imports
import numpy as np

# Enter solution here

def create_3d_array():
    arr = np.arange(27).reshape(3,3,3)
    N = np.size(arr)
    return arr 


