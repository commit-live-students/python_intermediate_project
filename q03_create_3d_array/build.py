# Default Imports
import numpy as np

# Enter solution here
def create_3d_array():
    nv = 3*3*3
    a = np.arange(nv)
    b = np.reshape(a,newshape=(3,3,3))
    return b
