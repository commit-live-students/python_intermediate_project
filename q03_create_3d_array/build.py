# %load q03_create_3d_array/build.py
# Default Imports
import numpy as np

# Enter solution here
import numpy as np
def create_3d_array():
    N= 3*3*3
    return np.arange(N).reshape((3, 3, 3))

create_3d_array()

