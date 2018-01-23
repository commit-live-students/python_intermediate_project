# Default imports
import numpy as np
from greyatomlib.python_intermediate.q01_zeros_array.build import  array_zeros

# Write your code
def array_reshaped_zeros():
    #print (array_zeros())
    zeros_array_reshaped = array_zeros().reshape(2,3,4)
    #print (zeros_array_reshaped)
    return zeros_array_reshaped
