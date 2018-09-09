# %load q03_create_3d_array/build.py
# Default Imports
import numpy as np

# Enter solution here

def create_3d_array():
    N = np.arange(27)
    array = np.array(N)
    array = array.reshape(3,3,3)
    
    return create_3d_array




