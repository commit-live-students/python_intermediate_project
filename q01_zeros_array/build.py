# %load q01_zeros_array/build.py
# Default Imports
import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir),  '..'  ))
import numpy as np

# Your solution
def array_zeros():
    zeros_array = np.zeros((3,4,2))
    return(zeros_array)
a = array_zeros()
clive submit python_intermediate_project:q01_zeros_array


