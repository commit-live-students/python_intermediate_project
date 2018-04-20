# %load q02_zeros_reshaped/build.py
# Default imports
import numpy as np
from greyatomlib.python_intermediate.q01_zeros_array.build import  array_zeros

def array_reshaped_zeros():
    zeros_array_reshaped=array_zeros()
    print(zeros_array_reshaped)
    return(zeros_array_reshaped.reshape(2,3,4))
    
# Write your code


