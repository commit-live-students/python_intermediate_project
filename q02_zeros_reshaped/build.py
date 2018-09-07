#%load q02_zeros_reshaped/build.py 
import numpy as np
def array_reshaped_zeros():
    
    arr=np.zeros((3,4,2))
    zeros_array_reshaped=arr.reshape((2,3,4))
    #print(arr1)
    return zeros_array_reshaped



