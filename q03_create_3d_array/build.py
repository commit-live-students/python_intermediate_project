# %load q03_create_3d_array/build.py
# Default Imports
import numpy as np

# Enter solution here
def create_3d_array():

    N=27
    arr = np.arange(N).reshape(3,3,3)
    print arr

    return arr

create_3d_array()
