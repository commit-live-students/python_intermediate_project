# Default Imports
import numpy as np

# Enter solution here
def create_3d_array():

    N = (3*3*3)
    array3 = np.arange(0, N)
    reshaped = array3.reshape(3,3,3)
    return reshaped
print create_3d_array()
