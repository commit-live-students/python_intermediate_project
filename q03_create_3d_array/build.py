# Default Imports
import numpy as np

def create_3d_array():
    a = len(np.zeros((3,3,3)))

    b = np.arange(0, a)

    reshaped = np.reshape(b, (3, 3, 3))
    print reshaped

    #b = np.reshape(a, (3, 3, 3))
    #print b
create_3d_array()
    
