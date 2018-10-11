# %load q03_create_3d_array/build.py
# Default Imports
import numpy as np

# Enter solution here
def create_3d_array():
    
    actual = [
            [[0, 1, 2],
             [3, 4, 5],
             [6, 7, 8]],

            [[9, 10, 11],
             [12, 13, 14],
             [15, 16, 17]],

            [[18, 19, 20],
             [21, 22, 23],
             [24, 25, 26]]
        ]
    var = np.array(actual)        
#N = var.size
    N = np.count_nonzero(var)
    array2 = np.arange(N-1)
    var.reshape((3,3,3))
    return var
create_3d_array()




