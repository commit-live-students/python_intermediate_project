# %load q03_create_3d_array/build.py
# Default Imports
import numpy as np

# Enter solution here
def create_3d_array():
    n = 3*3*3
    array = np.arange(n)
    print (array.reshape(3,3,3))
    return array.reshape(3,3,3)
   
create_3d_array()


