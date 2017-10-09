# Default Imports
import numpy as np

# Enter solution hereimport numpy as np


def create_3d_array():
    N = range(27)
    b = np.array(N)
    b.resize(3,3,3)
    return(b)
