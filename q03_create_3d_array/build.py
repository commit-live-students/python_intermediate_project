# Default Imports
import numpy as np

# Enter solution here
def create_3d_array():
    dim = (3,3,3)
    nDarr = np.asarray([i for i in range(np.size(np.ndarray(dim)))])
    return np.reshape(nDarr,dim)
