# %load q01_zeros_array/build.py
# Default Imports
import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir),  '..'  ))
import numpy as np

# Your solution
def array_zeros() :
    s = (3, 4, 2)
    zeros_array=np.zeros(s)
    return(zeros_array)

    








