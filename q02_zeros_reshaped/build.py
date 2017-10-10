# %load q02_zeros_reshaped/build.py
# Default imports
import numpy as np
from greyatomlib.python_intermediate.q01_zeros_array.build import  array_zeros

def array_reshaped_zeros():
    zero_arrays = array_zeros()
    zeros_array_reshaped = np.reshape(zero_arrays,(2,3,4))

    return zeros_array_reshaped

# Write your code
array_reshaped_zeros()
