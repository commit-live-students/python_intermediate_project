# Default Imports
import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir),  '..'  ))
import numpy as np
import numpy.random as rd
def array_zeros():
    zeros_array = np.zeros(shape=[3, 4, 2])
    #zeros_array = [i*0 for i in zeros_array]
    return zeros_array


# Your solution
