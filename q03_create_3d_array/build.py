# Default Imports
import numpy as np

# Enter solution here
def create_3d_array() :
    n = np.zeros(shape=(3,3,3)).size
    b = np.reshape(np.arange(n),(3,3,3))
    return b
