# %load q03_create_3d_array/build.py
# Default Imports
import numpy as np

def create_3d_array():
    total_elements = 3 * 3 * 3
    array_1d = np.arange(total_elements)
    return array_1d.reshape(3, 3, 3)

    


