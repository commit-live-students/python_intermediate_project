import numpy as np

def create_3d_array():
    temp_arr = np.ones((3,3,3))
    N = temp_arr.size
    Narr = np.arange(0,N).reshape(3,3,3)
    return Narr



