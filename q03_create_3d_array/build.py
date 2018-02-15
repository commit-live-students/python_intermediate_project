# Default Imports
import numpy as np
import random
# Enter solution here
def create_3d_array():
    a = np.zeros((3,3,3))
    N = a.size
    reshaped_3d_array = np.arange(0,N).reshape((3,3,3))
    return reshaped_3d_array
