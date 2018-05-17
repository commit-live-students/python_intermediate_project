# %load q03_create_3d_array/build.py
# Default Imports
import numpy as np

# Enter solution here

def create_3d_array():
    
    array1 = np.arange(0, 27, dtype=np.int)
    
    return array1.reshape(3,3,3)

create_3d_array()
    


