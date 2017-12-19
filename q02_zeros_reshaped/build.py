# Default imports
import numpy as np
from greyatomlib.python_intermediate.q01_zeros_array.build import  array_zeros

# Write your code

# Write your code
def array_zeros():
    zeros_array = np.zeros((3,4,2), dtype = np.int16)
    return zeros_array

def array_reshaped_zeros():
    var = np.zeros((2,3,4), dtype = np.int16)
    return var
