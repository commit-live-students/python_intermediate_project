# %load q03_create_3d_array/build.py
# Default Imports
import numpy as np

# Enter solution here
def create_3d_array():
    n = 3 * 3* 3
#     print(n)
    td_array = np.arange(0,27,1).reshape((3,3,3))
    return td_array
    
create_3d_array()


