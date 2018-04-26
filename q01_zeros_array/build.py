# %load q01_zeros_array/build.py
# Default Imports
import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir),  '..'  ))
import numpy as np
def array_zeros():
    zeros_array=np.arange(24)
    zeros_array=zeros_array.reshape(3,4,2)*0
    return zeros_array
    
# Your solution





