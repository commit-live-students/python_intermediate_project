import numpy as np
from greyatomlib.python_intermediate.q01_zeros_array.build import array_zeros

def array_reshaped_zeros(): 
    
    zeros_array_reshaped = array_zeros().reshape(2,3,4)
    return zeros_array_reshaped
testArray = array_reshaped_zeros()
print(testArray)


