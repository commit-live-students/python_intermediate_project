# Default imports
import numpy as np
from greyatomlib.python_intermediate.q01_zeros_array.build import  array_zeros

# Write your code
def array_reshaped_zeros():
    arr1 = array_zeros()
    #arr1
    arr2 = arr1.reshape(2,3,4)
    return arr2

array_reshaped_zeros()
