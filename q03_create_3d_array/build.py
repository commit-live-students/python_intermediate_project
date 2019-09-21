# Default Imports
import numpy as np

def create_3d_array():
    arr_random=np.random.rand(3,3,3)
    N=np.count_nonzero(arr_random)
    arr=np.arange(N).reshape(3,3,3)
    return arr
