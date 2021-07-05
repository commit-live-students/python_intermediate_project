# %load q02_zeros_reshaped/build.py
# Default imports
import numpy as np
from greyatomlib.python_intermediate.q01_zeros_array.build import  array_zeros

# Write your code
def array_reshaped_zeros():
    a = array_zeros()
    return a.reshape(2,3,4)
    
b =array_reshaped_zeros()
# %clive submit python_intermediate_project:q02_zeros_reshaped


