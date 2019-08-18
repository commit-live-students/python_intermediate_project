import numpy as np

def create_3d_array():
    a=range(27)
    b=np.array(a)
    c = b.reshape(3,3,3)
    return c

create_3d_array()
