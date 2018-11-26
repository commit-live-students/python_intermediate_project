# %load q03_create_3d_array/build.py
# Default Imports
import numpy as np

# Enter solution here
def create_3d_array():
    one_dim_array = np.array(list(range(0,27)))
    three_dim_array = np.reshape(one_dim_array, (3,3,3))
    return three_dim_array

create_3d_array()


