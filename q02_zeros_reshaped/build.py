# Default imports
import numpy as np
from greyatomlib.python_intermediate.q01_zeros_array.build import  array_zeros

# Write your code

def array_reshaped_zeros():
    original = array_zeros()
    zeros_array_reshaped = original.reshape(2,3,4)

    return zeros_array_reshaped
