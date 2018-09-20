# %load q03_create_3d_array/build.py
# Default Imports
import numpy as np

# Enter solution here
def create_3d_array():
    n = 3**3
    x = np.array(range(n)).reshape((3,3,3))
    return x
create_3d_array()

