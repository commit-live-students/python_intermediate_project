import numpy as np
def create_3d_array():
    a1 = np.arange(27)
    a2 = a1.size
    a3 = a1.reshape(3,3,3)
    #print a1
    #print a3
    #print type(a3)
    return a3
