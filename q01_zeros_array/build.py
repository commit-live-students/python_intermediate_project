import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir),  '..'  ))
import numpy as np

# Your solution
def array_zeros():
    zeros_array = np.zeros([3, 4, 2])

    return zeros_array
    #print type(zeros_array)
print array_zeros()
