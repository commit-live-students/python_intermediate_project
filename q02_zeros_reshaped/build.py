# %load q02_zeros_reshaped/build.py
# Default imports
import numpy as np
from greyatomlib.python_intermediate.q01_zeros_array.build import  array_zeros

def array_reshaped_zeros():
    zeros_array= np.zeros([3,4,2])
    zeros_array_reshaped = np.reshape(zeros_array,[2,3,4])
    
    return zeros_array_reshaped
array_reshaped_zeros()



