# Default Imports
import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir),  '..'  ))
import numpy as np

# Your solution
def array_zeros():
    zeros_array=np.zeros((3,4,2))

    return zeros_array

def array_reshaped_zeros():
    zeros_array_reshaped = array_zeros().reshape((2,3,4))

    return zeros_array_reshaped

print array_reshaped_zeros()
