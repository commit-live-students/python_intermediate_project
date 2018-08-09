# %load q03_create_3d_array/build.py
# Default Imports
import numpy as np

# Enter solution here
def create_3d_array():
    x=np.arange(27)
    return x.reshape(3,3,3)
create_3d_array()

