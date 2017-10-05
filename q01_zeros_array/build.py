# Default Imports
import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir),  '..'  ))
import numpy as np

#zeros_array = [[0,0,0],[0,0,0,0],[0,0]]

def array_zeros():
    global zeros_array
    zeros_array = np.zeros((3, 4, 2))
#    zeros_array = np.array(zeros_array)
    return zeros_array
