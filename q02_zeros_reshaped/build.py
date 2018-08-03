# %load q02_zeros_reshaped/build.py
# Default imports
import numpy as np
from greyatomlib.python_intermediate.q01_zeros_array.build import  array_zeros

def array_reshaped_zeros():
    arr= array_zeros()
    zeros_array_reshaped=np.reshape(arr,(2,3,4))
    return zeros_array_reshaped

array_reshaped_zeros()



