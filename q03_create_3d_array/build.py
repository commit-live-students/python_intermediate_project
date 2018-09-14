# %load q03_create_3d_array/build.py
# Default Imports
import numpy as np

# Enter solution here
def create_3d_array():
    n = 27
    arr = np.array(range(n))
    return arr.reshape((3,2,2))

actual = [
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
arr = create_3d_array()

np.all(arr == actual)

