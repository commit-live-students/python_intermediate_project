# Default Imports
import numpy as np
def create_3d_array():
    N = 3 * 3 * 3
    Array = np.arange(N)
    ReshapedArray = Array.reshape(3,3,3)
    return ReshapedArray
# Enter solution here
