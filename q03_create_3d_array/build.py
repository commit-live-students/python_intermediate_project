# Default Imports
import numpy as np

# Enter solution here
def create_3d_array():
    N = 3*3*3
    arr1 = np.arange(0,N)
    #print arr1
    arr2 = arr1.reshape(3,3,3)
    #print arr2
    return arr2

create_3d_array()
