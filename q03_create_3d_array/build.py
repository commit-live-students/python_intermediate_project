# Default Imports
import numpy as np

# Enter solution here
def create_3d_array():
    N=27
    array_a = [range(0,N)]
    np_array = np.array(array_a)
    return np.resize(np_array,(3,3,3))
