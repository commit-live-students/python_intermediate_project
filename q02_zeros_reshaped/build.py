# Default imports
import numpy as np
from greyatomlib.python_intermediate.q01_zeros_array.build import  array_zeros

# Write your code
def array_reshaped_zeros():
    arr = array_zeros()
    print(arr)
    return arr.reshape(2,3,4)
