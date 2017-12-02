# Default imports
import numpy as np
from greyatomlib.python_intermediate.q01_zeros_array.build import  array_zeros

# Write your code
zeros_array_reshaped = array_zeros()
def array_reshaped_zeros():
    return np.reshape(zeros_array_reshaped, (2, 3, 4))
