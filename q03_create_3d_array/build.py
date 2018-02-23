# Default Imports
import numpy as np

# Enter solution here
def create_3d_array():
    arr = np.arange(27)
    arr1 = arr.reshape(3,3,3)
    return arr1

print create_3d_array()
