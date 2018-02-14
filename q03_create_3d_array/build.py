# Default Imports
import numpy as np

# Enter solution here
def create_3d_array():
    N = np.arange(27)
    N1 = N.reshape((3,3,3))
    return(N1)
print(create_3d_array())
