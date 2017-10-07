# Default Imports
import numpy as np

# Enter solution here
def create_3d_array():
    N = 27
    arr = np.arange(0,N)
    arr_reshaped = arr.reshape((3,3,3))

    return arr_reshaped
print create_3d_array()
