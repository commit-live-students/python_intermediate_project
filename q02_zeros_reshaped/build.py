# Default imports
import numpy as np
from greyatomlib.python_intermediate.q01_zeros_array.build import  array_zeros

def array_reshaped_zeros():
    return np.zeros(shape=(3,4,2)).reshape(2,3,4)

print array_reshaped_zeros()
