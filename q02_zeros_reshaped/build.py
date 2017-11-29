# Default imports
import numpy as np
from greyatomlib.python_intermediate.q01_zeros_array.build import  array_zeros

# Write your code
def array_reshaped_zeros():

    arr1 = array_zeros()
    zeros_array_reshaped = arr1.reshape(2,3,4)

    return zeros_array_reshaped

print array_reshaped_zeros()
