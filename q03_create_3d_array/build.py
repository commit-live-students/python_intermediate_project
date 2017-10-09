import numpy as np

# Enter solution here
def create_3d_array():
    result = np.arange(0,27)
    result = result.reshape(3,3,3)
    return result
