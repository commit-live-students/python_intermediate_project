# %load q02_zeros_reshaped/build.py
# Default imports
import numpy as np
from greyatomlib.python_intermediate.q01_zeros_array.build import  array_zeros

def array_reshaped_zeros():
    zeros = np.zeros([3,4,2])
    reshape = zeros.reshape([2,3,4])
    return (reshape)
array_reshaped_zeros()


