# %load q03_create_3d_array/build.py
# Default Imports
import numpy as np

# create 3 d array from 0 to 26 
def create_3d_array():
    array = np.arange(0,27).reshape((3,3,3))
    return array

if __name__ == '__main__':
    create_3d_array()
    print(create_3d_array())


