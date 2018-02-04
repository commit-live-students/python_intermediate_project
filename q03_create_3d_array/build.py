# Default Imports
import numpy as np

def create_3d_array():
    c = np.zeros((3, 3, 3))
    N = c.size

    reshaped = np.arange(N).reshape(3, 3, 3)
    return reshaped


create_3d_array()
