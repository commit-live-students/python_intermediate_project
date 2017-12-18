# Default Imports
import numpy as np
def create_3d_array():
    oness = np.ones((3,3,3),dtype=np.int16)
    a0 = np.count_nonzero(oness)
    a1 = np.arange(a0)
    arr = a1.reshape(3,3,3)
    return arr
