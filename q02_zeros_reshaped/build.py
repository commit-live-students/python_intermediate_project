# Default imports
import numpy as np
from greyatomlib.python_intermediate.q01_zeros_array.build import  array_zeros


def array_reshaped_zeros():
    zeros_array_reshaped = array_zeros()
    zeros_array_reshaped = zeros_array_reshaped.reshape(2,3,4)
    return zeros_array_reshaped
