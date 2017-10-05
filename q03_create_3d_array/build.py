# %load q03_create_3d_array/build.py
# Default Imports
import numpy as np
# Enter solution here

def create_3d_array():
    #create an array of 3 dimension
    #number of values that can be store=3*3*3=27
    return np.arange(0,27,1).reshape(3,3,3)
