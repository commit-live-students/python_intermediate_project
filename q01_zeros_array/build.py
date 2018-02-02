# Default Imports
import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir),  '..'  ))
import numpy as np

# Your solution

def array_zeros():
    zeros_array = np.zeros((3,4,2))#12).reshape(3,4)
    #print zeros_array
    #print zeros_array.shape
    #print type(zeros_array)
    return zeros_array

#array_zeros()
