# Default Imports
import numpy as np

# Enter solution here
def create_3d_array():
    a = np.arange(0,27)
    b = a.reshape(3,3,3)
    #print b
    return b

create_3d_array()
