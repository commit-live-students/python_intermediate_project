# Default imports
import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
import numpy as np

# Your solution
# Your code here
def array_zeros():
    zeros_array = np.zeros(shape=(3, 4, 2))
    return zeros_array

array_zeros()
