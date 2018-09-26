# %load q03_create_3d_array/build.py
# Default Imports
import numpy as np


def create_3d_array():
    a=np.arange(0,27)
    a=a.reshape(3,3,3)
    return a
    
    
    


