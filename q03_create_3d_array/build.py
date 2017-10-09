# Default Imports
import numpy as np


def create_3d_array():
    N =27
    array = np.arange(0 ,N )
    array = array.reshape(3,3,3)
    return array
