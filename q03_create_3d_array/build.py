# %load q03_create_3d_array/build.py
# Default Imports
import numpy as np

# Enter solution here
def create_3d_array():
    list_1 = [
            [[0, 1, 2],
             [3, 4, 5],
             [6, 7, 8]],

            [[9, 10, 11],
             [12, 13, 14],
             [15, 16, 17]],

            [[18, 19, 20],
             [21, 22, 23],
             [24, 25, 26]]
        ]
    np.reshape(list_1, (3,3,3))
    return list_1

