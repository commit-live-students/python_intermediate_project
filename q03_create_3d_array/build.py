# %load q03_create_3d_array/build.py
# Default Imports
import numpy as np

# Enter solution here

def create_3d_array():
    total_elements = 3 * 3 * 3
    array_1d = np.arange(total_elements, dtype = np.int8)
    array_3d = array_1d.reshape(3,3,3)
    return array_3d
create_3d_array()

