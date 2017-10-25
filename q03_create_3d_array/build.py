# Default Imports
import numpy as np

# Enter solution here
def create_3d_array():
    N = 3*3*3
    arr = np.arange(N)
    return arr.reshape(3,3,3)

print create_3d_array()
