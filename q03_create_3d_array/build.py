# %load q03_create_3d_array/build.py
# Default Imports
import numpy as np

# Enter solution here

def create_3d_array():
    n = 3*3*3
    array1 = np.arange(n)
    array2 = array1.reshape(3,3,3)
    return array2

create_3d_array()


