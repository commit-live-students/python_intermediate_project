import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir),  '..'  ))
import numpy as np

def array_zeros():
    shape=(3,4,2)
    zeros_array = np.zeros((shape))
    return zeros_array

var = array_zeros()


