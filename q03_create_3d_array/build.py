# %load q03_create_3d_array/build.py
# Default Imports
import numpy as np

# Enter solution here
def create_3d_array():
    total_values = 3**3
    arr = np.arange(total_values).reshape((3,3,3))
    return arr

create_3d_array()    
