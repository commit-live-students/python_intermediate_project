# Default Imports
import numpy as np

# Enter solution here
def create_3d_array() :
    lst = list(range(0,27))
    arr = np.array(lst)
    arr2 = arr.reshape(3,3,3)
 #   print arr2
    return arr2
create_3d_array()
