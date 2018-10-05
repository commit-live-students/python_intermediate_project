# %load q03_create_3d_array/build.py
# Default Imports
import numpy as np

# Enter solution here
def create_3d_array():
    Count=3*3*3
    l1=list(range(0,Count,1))
    arr1=np.array(l1)
    arr2=arr1.reshape(3,3,3)
    print(arr2.shape)
    return arr2

