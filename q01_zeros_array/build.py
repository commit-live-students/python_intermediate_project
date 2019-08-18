# Default Imports
import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir),  '..'  ))
import numpy as np

def array_zeros():
    zeros_array = (3,4,2)
    zeros_array = np.zeros(zeros_array)
    return zeros_array

array_zeros()# Your solution
