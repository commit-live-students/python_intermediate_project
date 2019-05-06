# %load q03_create_3d_array/build.py
# Default Imports
import numpy as np

# Enter solution here
def create_3d_array():
    a=np.zeros((3,3,3))
    print(a)
    b=np.arange(a.size)
    print(b)
    b.shape=(((3,3,3)))
    return b

create_3d_array()
    


