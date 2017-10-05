# Default Imports
import numpy as np

# Enter solution here
def create_3d_array():
    lst = range(27)
    print lst
    arr = np.array(lst)
    return arr.reshape(3,3,3)
