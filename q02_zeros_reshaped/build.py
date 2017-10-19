# Default imports
import numpy as np
from greyatomlib.python_intermediate.q01_zeros_array.build import array_zeros

# Write your code
arr = array_zeros()
def array_reshaped_zeros():
    arr1 = np.reshape(arr, (2,3,4))
    return arr1
