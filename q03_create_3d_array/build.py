# Default Imports
import numpy as np

# Enter solution here
def create_3d_array():
    N = list(range(0,27))
    arry = np.array((N))
    reshp_arr = arry.reshape(3,3,3)
    return (reshp_arr)
