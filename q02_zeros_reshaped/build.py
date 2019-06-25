# %load q02_zeros_reshaped/build.py
# Default imports
import numpy as np
from greyatomlib.python_intermediate.q01_zeros_array.build import  array_zeros

# Write your code
def array_reshaped_zeros():
    #call the array zero function and apply reshape funtion
    zeros_array_reshaped = array_zeros().reshape((2,3,4))
    return zeros_array_reshaped

if __name__ == '__main__':
    array_reshaped_zeros()
    print(array_reshaped_zeros())


