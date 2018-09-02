# %load q03_create_3d_array/build.py
# Default Imports
import numpy as np

# Enter solution here
def create_3d_array():
    main_arr = np.arange(0,27)
    third_arr = np.reshape(main_arr,(3,3,3))
    return third_arr
create_3d_array()



