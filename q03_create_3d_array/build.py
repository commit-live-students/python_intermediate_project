import numpy as np
def create_3d_array():
    a=np.arange(0,27)
    b=a.reshape(3,3,3)
    return b
    
c=create_3d_array()
c
c.shape


