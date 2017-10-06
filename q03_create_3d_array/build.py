# %load q03_create_3d_array/build.py
# Default Imports
import numpy as np
def create_3d_array():
    my_list=[]
    my_list=range(27)
    arr = np.array(my_list)
    rarr = np.reshape(arr,(3, 3, 3))
    return rarr

create_3d_array()

# Enter solution here
