# Default Imports
import numpy as np

# Enter solution here
def create_3d_array():
    arr = np.empty((3,3,3))
    N = arr.size
    arrTwo = np.arange(N).reshape((3,3,3))
    return arrTwo
