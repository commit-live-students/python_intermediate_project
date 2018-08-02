# %load q03_create_3d_array/build.py
# Default Imports
import numpy as np

def create_3d_array():
    N =3*3*3
    ar = np.arange(N)
    array3d = ar.reshape(3,3,3)
    return array3d

    







