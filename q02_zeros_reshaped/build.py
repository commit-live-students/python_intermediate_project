# Default imports
import numpy as np
from greyatomlib.python_intermediate.q01_zeros_array.build import  array_zeros

# Write your code
def array_reshaped_zeros():
    zeros_array_reshaped = np.reshape(array_zeros(), newshape=(2,3,4))
    #print zeros_array_reshaped
    #print type(zeros_array_reshaped)
    #print zeros_array_reshaped.shape
    return zeros_array_reshaped

#array_reshaped_zeros()
