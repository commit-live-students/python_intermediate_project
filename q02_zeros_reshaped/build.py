# %load q02_zeros_reshaped/build.py
# Default imports
import numpy as np
from greyatomlib.python_intermediate.q01_zeros_array.build import  array_zeros

# Write your code
def array_reshaped_zeros():
    zeros_array = np.random.rand(3,4,2)
    print zeros_array
    zeros_array_reshaped = zeros_array.reshape(2,3,4)
    print zeros_array_reshaped

    return zeros_array_reshaped

array_reshaped_zeros()
