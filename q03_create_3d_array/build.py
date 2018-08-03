# %load q03_create_3d_array/build.py
# Default Imports
import numpy as np

# Enter solution here
def create_3d_array():
    c = np.arange(27).reshape(3,3,3)
    return c

create_3d_array()

