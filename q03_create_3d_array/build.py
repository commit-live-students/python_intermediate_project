# Default Imports
import numpy as np

# Enter solution here
def create_3d_array():
    n1 = np.zeros((3,3,3))
    N = n1.size
    anum = np.arange(N)
    array3d = anum.reshape((3,3,3))
    return array3d
