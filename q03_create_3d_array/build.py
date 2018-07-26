# %load q03_create_3d_array/build.py
# Default Imports
import numpy as np

# Enter solution here
def create_3d_array():
    ndimarray = np.arange(0, 27)
    ndimarray.shape = (3, 3, 3)
    
    return ndimarray


