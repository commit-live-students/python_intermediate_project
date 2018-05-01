
import numpy as np 
def create_3d_array():
    N = 28
    a =np.arange(0,N-1)
    b = a.reshape(3,3,3)
    return b
create_3d_array()


