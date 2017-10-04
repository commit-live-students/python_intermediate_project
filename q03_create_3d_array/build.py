# Default Imports
import numpy as np
def create_3d_array():
    dimensions = 3
    length = 3
    arr = np.arange(length**dimensions)

    return arr.reshape((3,3,3)) 
# Enter solution here
