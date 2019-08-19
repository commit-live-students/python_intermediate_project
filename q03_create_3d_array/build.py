# Default Imports
import numpy as np

def create_3d_array():
    x = np.arange(27).reshape((3,3,3))
    x.reshape(9,3,1).swapaxes(2,0)
    return x

create_3d_array()
# Enter solution here
