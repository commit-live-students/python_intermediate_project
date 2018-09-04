# %load q03_create_3d_array/build.py
# Default Imports
import numpy as np

# Enter solution here
def create_3d_array():
    zeros_array = np.zeros((3,3,3))
    array = np.arange(27)
    print(array)
    array_reshaped = array.reshape((3,3,3))
    print(array_reshaped)
    return array_reshaped

    
create_3d_array()



