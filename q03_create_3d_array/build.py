# Default Imports
import numpy as np

# Enter solution here
def create_3d_array():
    N=3*3*3
    array_a = np.array((range(N)))
    array_a = array_a.reshape((3,3,3))
    return array_a
print create_3d_array()
