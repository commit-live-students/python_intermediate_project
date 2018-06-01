# %load q03_create_3d_array/build.py
# Default Imports
import numpy as np

# Enter solution here
def create_3d_array():
    n = 28
    x = np.arange(0,n-1)
    y = np.array(x.reshape(3,3,3))
    return y

