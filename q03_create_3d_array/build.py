# Default Imports
import numpy as np

def create_3d_array():
    a = np.zeros(shape=(3,3,3))
    #print a
    array = np.size(a)
    print array
    array_number =  np.arange(0,27)
    print array_number
    variable = np.reshape(array_number,newshape = (3,3,3))
    return variable

print create_3d_array()
