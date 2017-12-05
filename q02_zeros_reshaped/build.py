# Default imports
import numpy as np
from greyatomlib.python_intermediate.q01_zeros_array.build import  array_zeros

# Write your code
def array_reshaped_zeros():
    zeros_array = np.zeros([3,4,2])
    zeros_array_reshaped=zeros_array.reshape(zeros_array.shape[2],zeros_array.shape[0],zeros_array.shape[1])
    return zeros_array_reshaped

print array_reshaped_zeros()
