# %load q03_create_3d_array/build.py
# Default Imports
import numpy as np

# Enter solution here
def create_3d_array():
    array_demo = np.random.rand(3,3,3)
    n = array_demo.size
    arr = np.arange(0,n,1)
    arr = arr.reshape(3,3,3)
    return arr

create_3d_array()

