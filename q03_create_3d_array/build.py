# Default Imports
import numpy as np

# Enter solution here
def create_3d_array():
    n = int(raw_input('Enter number of values to be stored in array : '))# number of elements inn array
    a = np.arange(n).reshape((3,3,3))
    print a

    #np.arange(n).reshape((3,3))

create_3d_array()
