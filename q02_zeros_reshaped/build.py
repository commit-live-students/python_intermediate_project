# %load q02_zeros_reshaped/build.py
# Default imports
import numpy as np
from greyatomlib.python_intermediate.q01_zeros_array.build import array_zeros

# Write your code
def array_reshaped_zeros():
    arra1 = array_zeros()
    zeros_array_reshaped = arra1.reshape([2,3,4])
    return zeros_array_reshaped
arra1 = np.zeros([3,4,2])
arra1
arra2 = arra1.reshape([2,3,4])
arra2
array_reshaped_zeros()

