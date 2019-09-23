# Default imports
import numpy as np
from greyatomlib.python_intermediate.q01_zeros_array.build import  array_zeros

def array_reshaped_zeros():
    zero_array = array_zeros()
    reshaped_array = zero_array.reshape(2,3,4)
    return reshaped_array

#print array_reshaped_zeros()
