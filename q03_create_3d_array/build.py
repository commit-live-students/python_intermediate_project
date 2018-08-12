# %load q03_create_3d_array/build.py
# Default Imports
import numpy as np

# Enter solution here
def create_3d_array():
    N=28
    arr = np.arange(0,(N-1))
    arr2 = arr.reshape((3,3,3))
    print(arr2)
    return arr2

create_3d_array()

