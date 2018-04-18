# %load q03_create_3d_array/build.py
# Default Imports
import numpy as np

# Enter solution here
def create_3d_array():
    array_3d = np.arange(27)
    array_3d = array_3d.reshape(3,3,3)
    return array_3d
create_3d_array()    


