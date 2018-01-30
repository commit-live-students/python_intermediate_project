# %load q03_create_3d_array/build.py
# Default Imports
import numpy as np

def create_3d_array():
    A = np.arange(27).reshape((3,3,3)) #1
    N = A.size #1
    Z = np.arange(N) #2
    return Z.reshape((3,3,3))

