import numpy as np


def array_zeros():
    zeros_array = np.array([3,4,2])
    return np.zeros(zeros_array) 

def array_reshaped_zeros():
    zeros_array_reshaped = ar_zeros.reshape([2,3,4])
    return zeros_array_reshaped 

ar_zeros = array_zeros()
print(ar_zeros)
ar_zeros_reshaped = array_reshaped_zeros()
print ('zeros_array_reshaped  : ',ar_zeros_reshaped )


