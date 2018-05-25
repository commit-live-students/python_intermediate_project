# %load q03_create_3d_array/build.py
# Default Imports
import numpy as np

# Enter solution here
def create_3d_array():
    count=3*3*3
    variable = np.arange(0,count).reshape(3,3,3)
    return variable

