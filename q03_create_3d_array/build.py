# Default Imports
import numpy as np

def create_3d_array():
    n = np.empty((3,3,3)).size
    array1=np.arange(n)
    array1=array1.reshape(3,3,3)
    return array1
