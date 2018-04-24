# %load q03_create_3d_array/build.py
# Default Imports
import numpy as np

# Enter solution here
def create_3d_array():
    arr=np.zeros((3,3,3))
    print(arr)
    print(len(arr))
    N=1
    for dim in np.shape(arr): N *= dim
    print(N)
    arr2=np.arange(0,N)
    print(arr2)
    arr2=arr2.reshape(3,3,3)
    return arr2
create_3d_array()
