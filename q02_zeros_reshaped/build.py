# %load q02_zeros_reshaped/build.py
# Default imports
import numpy as np
from greyatomlib.python_intermediate.q01_zeros_array.build import  array_zeros

# Write your code
def array_reshaped_zeros():
    zeros_array = array_zeros()
    reshaped_array = np.reshape(zeros_array, (2,3,4))
    return reshaped_array
array_reshaped_zeros()


