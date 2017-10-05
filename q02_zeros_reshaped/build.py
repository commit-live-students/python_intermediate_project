# Default imports
import numpy as np
from greyatomlib.python_intermediate.q01_zeros_array.build import  array_zeros

def array_reshaped_zeros():
    zero_array = array_zeros()
    zero_array_reshaped = zero_array.reshape((2,3,4))
    return zero_array_reshaped


# Write your code
