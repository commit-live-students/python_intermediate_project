# Default Imports
import numpy as np

# Enter solution here
def create_3d_array():
    N = 27
    nparray = np.arange(start=0, stop=27, dtype=np.int).reshape(3,3,3)
    #nparray = np.zeros((0,N-1))
    return nparray

print create_3d_array()
