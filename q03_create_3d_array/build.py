# %load q03_create_3d_array/build.py
# Default Imports
import numpy as np

# Enter solution here
def create_3d_array():
    N=3*3*3
    array=np.arange(N)
    return array.reshape(3,3,3)



