# Default Imports
import numpy as np

# Enter solution here
def create_3d_array():
    N=(np.ones((3,3,3))).size
    new = np.arange(N)
    new1 = new.reshape(3,3,3)
    return new1
