# Default Imports
import numpy as np

# Enter solution here
def create_3d_array():

    n=27
    temp=np.arange(0,n)

    variable=temp.reshape(3,3,3)
    return variable

print create_3d_array()
