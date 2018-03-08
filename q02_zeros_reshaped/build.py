# Default imports
import numpy as np
from greyatomlib.python_intermediate.q01_zeros_array.build import  array_zeros

# Write your code
def array_reshaped_zeros():
        n1 = np.zeros
        zeros_array_reshaped = np.zeros((3,4,2)).reshape((2,3,4))
        return zeros_array_reshaped

print array_reshaped_zeros()
