# %load q02_zeros_reshaped/build.py
# Default imports
import numpy as np
from greyatomlib.python_intermediate.q01_zeros_array.build import  array_zeros

# Write your code
def array_zeroes():
    zeros_array = np.zeros((3,4,2))
    return zeros_array
def array_reshaped_zeros():
    zeros_array_reshaped = np.zeros((2,3,4))
    return zeros_array_reshaped
print('Zero arrays with dimension(3,4,2)')
print(array_zeros())
print(' ')
print('Zero arrays after Reshape with dimensions (2,3,4)')
print(array_reshaped_zeros())


