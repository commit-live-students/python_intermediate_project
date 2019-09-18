# %load q02_zeros_reshaped/build.py
# Default imports
import numpy as np
from greyatomlib.python_intermediate.q01_zeros_array.build import  array_zeros

# Write your code
def array_zeros():
    zeros_array = np.zeros((3,4,2))
    return zeros_array

def array_reshaped_zeros():
    arr = array_zeros()
    zeros_array_reshaped = arr.reshape(2,3,4)
    return zeros_array_reshaped

# Your solution

reshaped_arr = array_reshaped_zeros()

print reshaped_arr
print reshaped_arr.shape
