# Default Imports
import numpy as np

def create_3d_array():
    count = 27

    array_values = np.arange(0,count)

    desired_array = array_values.reshape((3,3,3))
    return desired_array

create_3d_array()
