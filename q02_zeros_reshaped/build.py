# %load q02_zeros_reshaped/build.py
# Default imports
import numpy as np
from greyatomlib.python_intermediate.q01_zeros_array.build import  array_zeros

def array_reshaped_zeros():    
    zeros_array = (
        ((1,2),
         (3,4),
         (5,6),
         (7,8)),
        ((11,12),
         (13,14),
         (15,16),
         (17,18)),
        ((11,12),
         (13,14),
         (15,16),
         (17,18)),
    )
    d = np.array(zeros_array)
    a = np.zeros((3,4,2)) #another array
    d = a
    zeros_array_reshaped = np.reshape(d, (2,3,4))
    return zeros_array_reshaped

