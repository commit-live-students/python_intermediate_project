# %load q02_zeros_reshaped/build.py
# Default imports
import numpy as np
from greyatomlib.python_intermediate.q01_zeros_array.build import  array_zeros

def array_reshaped_zeros():
    ndr=array_zeros()
    ndr.shape=(3,4,4)
    return ndr
    
# Write your code

array_reshaped_zeros()


