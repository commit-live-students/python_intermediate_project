# Default Imports
import numpy as np
def create_3d_array():
    N=np.count_nonzero(np.ones((3,3,3)))
    arr=np.arange(N)
    arr=arr.reshape(3,3,3)

    return arr
# Enter solution here
