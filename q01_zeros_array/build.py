# %load q01_zeros_array/build.py
# Default Imports
import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir),  '..'  ))
import numpy as np

# Your solution
def array_zeros():
    zeros_array=np.array([3,4,2])
    zeros_array=np.zeros(zeros_array)
    return zeros_array
array_zeros()

array_zeros

