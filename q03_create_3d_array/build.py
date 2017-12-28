# Default Imports
import numpy as np

def create_3d_array():
    count =np.arange(0, 27)
    new_array=count.reshape((3,3,3))
    return new_array
