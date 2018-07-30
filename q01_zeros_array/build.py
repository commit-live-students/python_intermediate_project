# %load q01_zeros_array/build.py
# Default Imports
import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir),  '..'  ))
import numpy as np

# Your solution
def array_zeros():
    return np.zeros((3, 4, 2))

var = array_zeros()
# var.max() == 0
# var.shape
type(var)


