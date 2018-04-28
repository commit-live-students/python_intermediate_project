# %load q02_zeros_reshaped/build.py
# Default imports
import numpy as np
from greyatomlib.python_intermediate.q01_zeros_array.build import  array_zeros
def array_reshaped_zeros():
    zeros_array_reshaped=np.zeros(24)
    zeros_array_reshaped=zeros_array_reshaped.reshape(2,3,4)
    return  zeros_array_reshaped

    
        
# Write your code



