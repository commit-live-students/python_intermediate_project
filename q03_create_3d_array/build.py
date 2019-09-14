# Default Imports
import numpy as np

# Enter solution here
def create_3d_array():
    array=np.zeros((3,3,3))
    N=array.size
    array2=np.arange(N)
    array3=array2.reshape(3,3,3)
    return array3
