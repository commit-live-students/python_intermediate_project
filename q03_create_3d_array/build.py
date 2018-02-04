# Default Imports
import numpy as np

# Enter solution here
def create_3d_array():
    N = 27
    n1 = np.array(np.arange(N))
    return  np.reshape(n1, (3,3,3,))
