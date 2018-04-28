# %load q02_zeros_reshaped/build.py
# Default imports
import numpy as np
from greyatomlib.python_intermediate.q01_zeros_array.build import  array_zeros

# Write your code
def array_reshaped_zeros(x,y,z):
    s = (x,y,z)
    zeros_array=np.zeros(s)
    zeros_array=zeros_array.reshape((4,3,2)).transpose()
    return zeros_array
        

print(array_reshaped_zeros(3,4,2))




