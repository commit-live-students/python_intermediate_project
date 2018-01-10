# Default Imports
import numpy as np

# Enter solution here
def create_3d_array():

    N = (np.zeros((3,3,3), dtype=np.int32)).size
    array = np.arange(0, N)
    reshape_array = array.reshape(3,3,3)
    return reshape_array
