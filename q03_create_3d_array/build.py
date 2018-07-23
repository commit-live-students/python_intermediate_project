# %load q03_create_3d_array/build.py
# Default Imports
import numpy as np

def create_3d_array():
    N=3*3*3
    a=np.arange(N)
    b=a.reshape(3,3,3)
    return b

print(create_3d_array())
 


# Enter solution here


