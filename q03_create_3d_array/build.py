# %load q03_create_3d_array/build.py
# Default Imports
import numpy as np

# Enter solution here
def create_3d_array():
    #specify desired dimensions
    dim1 = 3; dim2 = 3; dim3 = 3
    elements = dim1*dim2*dim3
    variable = np.arange(elements).reshape(dim1,dim2,dim3)
    return variable
    
    


