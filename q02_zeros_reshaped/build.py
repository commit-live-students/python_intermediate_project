# Default imports
import numpy as np
from greyatomlib.python_intermediate.q01_zeros_array.build import  array_zeros

# Write your code
def array_reshaped_zeros():
    a=(array_zeros())
    a=a.reshape(2,3,4)
    return a
#print(array_reshaped_zeros())
