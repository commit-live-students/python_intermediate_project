# Default Imports
import numpy as np

# Enter solution here
def create_3d_array():
    arraydim= np.array((3,3,3))
    return np.array(range(arraydim.prod())).reshape(arraydim)
 
