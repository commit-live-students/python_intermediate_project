# %load q03_create_3d_array/build.py
# Default Imports
import numpy as np

# Enter solution here

def create_3d_array():
    arr=np.arange(0,27)
    arr=arr.reshape(3,3,3)
    return arr

create_3d_array()


