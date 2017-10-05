# %load q01_zeros_array/build.py
# Default Imports
import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir),  '..'  ))
import numpy as np

# Your solution
def array_zeros():
    shape=(3,4,2)
    zeros_array = np.zeros(shape)
    print (zeros_array)
    return zeros_array
