# %load q03_create_3d_array/build.py
# Default Imports
import numpy as np

# Enter solution here
def create_3d_array():
    N = np.zeros((3, 3, 3)).size
    numbers = np.arange(0,N)
    return np.reshape(numbers,(3,3,3))

create_3d_array()



