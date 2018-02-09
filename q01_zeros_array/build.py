# Default Imports
import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir),  '..'  ))
import numpy as np

def array_zeros():
    array = np.zeros(shape=(3,4,2))
    return array

print array_zeros()
