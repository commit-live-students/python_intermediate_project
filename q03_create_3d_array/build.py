# %load q03_create_3d_array/build.py
# Default Imports
import numpy as np

# Enter solution here

def create_3d_array():
    X = np.array(range(27))
    Y = np.reshape(X,(3,3,3))
    return Y
create_3d_array()
    

