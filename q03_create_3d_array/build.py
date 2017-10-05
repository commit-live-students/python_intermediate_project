import numpy as np

def create_3d_array():
    n=3;
    elecount=27

    arr=np.array([i for i in range(0,27)])
    return arr.reshape((3,3,3))
