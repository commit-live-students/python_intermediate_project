# Default Imports
import numpy as np

# Enter solution here
def create_3d_array():
    n = 3**3

    array1 = np.arange(n).reshape(3,3,3)

    return array1
print create_3d_array()
