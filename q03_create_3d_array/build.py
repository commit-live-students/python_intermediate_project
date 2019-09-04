# Default Imports
import numpy as np

# Enter solution here
def create_3d_array():
    N=3*3*3
    A =np.arange(N)
    three_d_array=A.reshape(3,3,3)
    return three_d_array
