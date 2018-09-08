# %load q01_zeros_array/build.py
# Default Imports
import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir),  '..'  ))
import numpy as np
def array_zeros():
    zeros_array=np.zeros((3,4,2))
    return zeros_array
  n=(3,4,2)
zeros_array=np.array(n)
type(zeros_array)
np.zero(4)


