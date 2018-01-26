# Default Imports
import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir),  '..'  ))
import numpy as np

# return array of zeros with dimension as 3, 4, 2
def array_zeros():
    zeros_array = np.zeros((3,4,2),dtype=np.int8)
    return zeros_array
