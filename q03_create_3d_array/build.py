# %load q03_create_3d_array/build.py
# Default Imports
import numpy as np

# Enter solution here

def create_3d_array():
    N = np.arange(27)
    np.array(N)
    N = N.reshape(3,3,3)
    return N




