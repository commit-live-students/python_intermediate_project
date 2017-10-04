# Default Imports
import numpy as np

# Enter solution here
def create_3d_array(N=27):
    arr = np.arange(0,N)
    arr = arr.reshape((3,3,3))
    return arr
