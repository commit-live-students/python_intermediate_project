# %load q03_create_3d_array/build.py
# Default Imports
import numpy as np

# Enter solution here
def create_3d_array(): 
    N = 3*3*3
    a = np.arange(0, N)
    zeros_array = np.reshape(a,(3,3,3))
    print(zeros_array)

    return zeros_array
create_3d_array()



