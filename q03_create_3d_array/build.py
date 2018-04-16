import numpy as np

def create_3d_array():
    N = 28
    arr = np.arange(0,N-1)
    print(type(arr))
    new_arr = np.reshape(arr,(3,3,3))
    
    return new_arr


