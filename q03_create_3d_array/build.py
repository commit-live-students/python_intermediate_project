# %load q03_create_3d_array/build.py
# Default Imports
import numpy as np

# Enter solution here
def create_3d_array():
    
    
    N = 3 * 3 * 3
    
    arr = np.arange(N)
    
    arr1 = arr.reshape((3,3,3))
    
    #print(arr1)
    
    return arr1

create_3d_array()


