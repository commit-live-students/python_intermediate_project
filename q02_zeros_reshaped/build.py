# Default imports
import numpy as np
from greyatomlib.python_intermediate.q01_zeros_array.build import  array_zeros

# Write your code
def array_reshaped_zeros():
    Z = np.zeros((3,4,2))
    zeros_array_reshaped = Z.reshape((2,3,4))
    #zeros_array_reshaped
    #zeros_array_reshaped = array_zeros
    return zeros_array_reshaped
