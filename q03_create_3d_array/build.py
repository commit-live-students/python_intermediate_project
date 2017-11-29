# Default Imports
import numpy as np

def create_3d_array():
    initial_array = np.zeros((3,3,3))
    N = initial_array.size
    new_array= np.arange(0, N)
    desired_array = new_array.reshape((3,3,3))

    return desired_array
