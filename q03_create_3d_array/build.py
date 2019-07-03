# %load q03_create_3d_array/build.py
# Default Imports
import numpy as np


def create_3d_array():
    N=3*3*3
    array= np.arange(0,N,1).reshape(3,3,3)
    return array
print(create_3d_array())


