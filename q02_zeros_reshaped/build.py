import numpy as np
from greyatomlib.python_intermediate.q01_zeros_array.build import array_zeros
def array_reshaped_zeros():
    zeros_array = np.zeros((3,4,2),dtype=np.int16)
    array_reshaped_zeros = zeros_array.reshape(2,3,4)
    return array_reshaped_zeros
