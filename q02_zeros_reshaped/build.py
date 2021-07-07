# Default imports
import numpy as np
from greyatomlib.python_intermediate.q01_zeros_array.build import  array_zeros

a = array_zeros()
def array_reshaped_zeros():
    b = np.reshape(a,(2,3,4))
    return b
