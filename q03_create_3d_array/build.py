# %load q03_create_3d_array/build.py
# Default Imports
import numpy as np

# Enter solution here

def create_3d_array():
    original_array= np.zeros((3,3,3))
    N = original_array.size
    new_array= np.array(range(0,N))
    new_3d_array=new_array.reshape(3,3,3)
    
    return new_3d_array
create_3d_array()


