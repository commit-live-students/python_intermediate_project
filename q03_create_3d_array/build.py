# Default Imports
import numpy as np

# Enter solution here

def create_3d_array():
    N=27
    arr1=np.arange(0,N)
    arr2 = arr1.reshape(3,3,3)
    return arr2
