# %load q03_create_3d_array/build.py
# Default Imports
import numpy as np

def create_3d_array():
    vals = np.arange(0,27)
    reshapedd = vals.reshape([3,3,3])
    return reshapedd
create_3d_array()


