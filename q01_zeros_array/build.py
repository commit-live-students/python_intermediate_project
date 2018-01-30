# %load q01_zeros_array/build.py
# Default Imports
import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir),  '..'  ))
import numpy as np

# Your solution
def array_zeros():
    zeros_array = (
        ((1,2),
         (3,4),
         (5,6),
         (7,8)),
        ((11,12),
         (13,14),
         (15,16),
         (17,18)),
        ((11,12),
         (13,14),
         (15,16),
         (17,18)),
    )
    d = np.array(zeros_array)
    a = np.zeros((3,4,2))
    zeros_array = a
    return zeros_array


