# %load q02_zeros_reshaped/build.py
# Default imports
import numpy as np
from greyatomlib.python_intermediate.q01_zeros_array.build import  array_zeros

# Your solution
def array_zeros():
    zeros_array = np.zeros((3, 4,2))
    return zeros_array

def array_reshaped_zeros():
    zeros_array = array_zeros()
    array_reshaped_zeros = np.reshape(zeros_array,(2,3,4))
    return array_reshaped_zeros




