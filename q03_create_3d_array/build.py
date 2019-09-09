# Default Imports
import numpy as np

# Enter solution here
def create_3d_array():
    N=3*3*3
    #return np.arange(0,N).reshape((3,3,3))
    return np.reshape(np.arange(0,N),(3,3,3))
