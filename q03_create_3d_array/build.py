# Default Imports
import numpy as np

# Enter solution here
def create_3d_array():
    n=3**3
    array=np.array(range(n)).reshape((3,3,3))

    return array
