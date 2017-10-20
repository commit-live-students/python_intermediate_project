# Default Imports
import numpy as np

def create_3d_array():
    arr_z = np.zeros(shape=(3,3,3))
    N = arr_z.size
    arr = np.arange(0,N,1,dtype = 'int16')
    arr = arr.reshape(3,3,3)

    return arr
    
