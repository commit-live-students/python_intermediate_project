# %load q02_zeros_reshaped/build.py
# Default imports
import numpy as np
from greyatomlib.python_intermediate.q01_zeros_array.build import  array_zeros

# Write your code
def array_reshaped_zeros():
    var = array_zeros()
    return np.reshape(var, (2,3,4))

array_reshaped_zeros().shape == (2,3,4)


