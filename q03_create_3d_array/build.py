
# Default imports
import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir), '..','..'))
import numpy as np

# Write your code; here
def create_3d_array():
    ls = np.arange(0, 27, 1)
    arr = ls.reshape(3, 3, 3)
    return arr
