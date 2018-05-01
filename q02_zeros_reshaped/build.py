
import numpy as np
def array_reshaped_zeros():
    zeros_array = np.array([3,4,2])
    zeros_array_reshaped = np.zeros(zeros_array)
    #zeros_array_reshaped = zeros_array.reshape([2,3,4])
    return zeros_array_reshaped.reshape(2,3,4)
array_reshaped_zeros()


