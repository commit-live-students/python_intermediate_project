# Default imports
import numpy as np
from greyatomlib.python_intermediate.q01_zeros_array.build import  array_zeros

# Write your code
def array_reshaped_zeros():
    zeros_array = np.zeros((3, 4, 2))
    arr2 = zeros_array.reshape(2, 3, 4)
    return arr2

array_reshaped_zeros()
