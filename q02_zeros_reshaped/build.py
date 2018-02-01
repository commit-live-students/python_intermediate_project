# %load q02_zeros_reshaped/build.py
# Default imports
import numpy as np
from greyatomlib.python_intermediate.q01_zeros_array.build import  array_zeros

def array_reshaped_zeros ():
    np1=np.array(array_zeros()).flatten()
       
    zeros_array_reshaped= np1.reshape(2,3,4)
    #print np2.shape
   
    return zeros_array_reshaped

print array_reshaped_zeros ()
#print arr
# Write your code


