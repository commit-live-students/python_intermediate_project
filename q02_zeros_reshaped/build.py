# Default imports
import numpy as np
from greyatomlib.python_intermediate.q01_zeros_array.build import  array_zeros

# Write your code
def array_reshaped_zeros():
    az = array_zeros()
    ay = np.reshape(az,newshape=(2,3,4))
    #print ay
    #print(type(ay))
    return ay
#print array_reshaped_zeros()
