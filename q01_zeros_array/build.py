# Default Imports
import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir),  '..'  ))
import numpy as np

def array_zeros():
    zero_array = np.zeros((3,4,2))
    #print zero_array
    return zero_array
#array_zeros()
