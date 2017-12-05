# Default Imports
import numpy as np
import numpy.random as rd

# Enter solution here
def create_3d_array():
    N = 3*3*3
    array3d = np.arange(0,N)
    reshaped = array3d.reshape(3,3,3)
    return reshaped

print create_3d_array()
