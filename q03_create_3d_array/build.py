# Default Imports
import numpy as np

# Enter solution here
def create_3d_array():
    N = 3 * 3 * 3
    flat_array = np.arange(N)
    array_3d = flat_array.reshape(3,3,3)
    return array_3d

#print create_3d_array()
