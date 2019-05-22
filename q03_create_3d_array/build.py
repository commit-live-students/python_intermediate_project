import numpy as np

def create_3d_array():
    new_array = np.arange(27)
    new_array = new_array.reshape((3,3,3))
    return new_array
create_3d_array()    
