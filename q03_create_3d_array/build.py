# %load q03_create_3d_array/build.py
# Default Imports
import numpy as np

# Enter solution here
def create_3d_array():

    array1=np.arange(27)
    print (array1)
    array3d=array1.reshape(3,3,3)
    print (array3d)
    return(array3d)
    
    
create_3d_array()




