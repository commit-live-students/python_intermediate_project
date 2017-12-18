import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir),  '..'  ))
import numpy as np
def array_reshaped_zeros():
    zeros_array1 = np.zeros((3,4,2),dtype=np.int16)
    zeros_array_reshaped=zeros_array1.reshape((2,3,4))
    #print zeros_array
    #print type(zeros_array)
    return zeros_array_reshaped
