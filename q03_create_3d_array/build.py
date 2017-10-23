# Default Imports
import numpy as np

# Enter solution here

def create_3d_array():
    N = 28
    random_array = np.arange(N-1)
    reshaped_array = random_array.reshape((3,3,3))
    return reshaped_array
print create_3d_array()
