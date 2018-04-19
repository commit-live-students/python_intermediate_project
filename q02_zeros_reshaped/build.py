# %load q02_zeros_reshaped/build.py
# Default imports
import numpy as np
from greyatomlib.python_intermediate.q01_zeros_array.build import  array_zeros

# Write your code
def array_reshaped_zeros():
    zeroArray = array_zeros()
    zeroArrayReshaped = zeroArray.reshape((2,3,4))
    print(zeroArrayReshaped.shape)
    return zeroArrayReshaped

array_reshaped_zeros()


