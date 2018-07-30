# %load q03_create_3d_array/build.py
# Default Imports
import numpy as np

# Enter solution here
def create_3d_array():
    narray=np.array([x for x in range(27)])
    reshapedarray=np.reshape(narray,(3,3,3))
    return reshapedarray
create_3d_array()

