# Default Imports
import numpy as np

# Enter solution here

def create_3d_array():
    n=28
    arr=np.arange(n-1)
    arr=arr.reshape(3,3,3)
    #print(arr)
    return arr
create_3d_array()
