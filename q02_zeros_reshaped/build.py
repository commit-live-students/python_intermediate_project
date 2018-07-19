# %load q02_zeros_reshaped/build.py
# Default imports
import numpy as np
from greyatomlib.python_intermediate.q01_zeros_array.build import  array_zeros

def array_reshaped_zeros():
# Write your code
    zeros_array_reshaped=array_zeros()
    return zeros_array_reshaped.reshape(2,3,4)



