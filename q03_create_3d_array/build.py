# %load q03_create_3d_array/build.py
# Default Imports
import numpy as np

# Enter solution here
def create_3d_array():
    N=27
    arr=np.arange(N)
    variable= np.reshape(arr,(3,3,3))
    return variable
    
 

