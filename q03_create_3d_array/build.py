# Default Imports
import numpy as np
def create_3d_array():
    a = np.zeros((3,3,3))
    N = a.size
   # print N
    reshaped = np.arange(N).reshape(3,3,3)
   # print reshaped
    return reshaped
create_3d_array()
