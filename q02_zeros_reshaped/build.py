# %load q02_zeros_reshaped/build.py
# Default imports
import numpy as np
from greyatomlib.python_intermediate.q01_zeros_array.build import  array_zeros

# Write your code

arr1 = np.arange(0,9).reshape((3,3))
arr1
def array_reshaped_zeros(arr = array_zeros()):
    return arr.reshape(((2,3,4)))
array_reshaped_zeros()


