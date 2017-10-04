# Default Imports
import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir),  '..'  ))
import numpy as np

# Your solution
#def func() :
#    arr = [[[0,0],[0,0],[0,0],[0,0]],[[0,0],[0,0],[0,0],[0,0]],[[0,0],[0,0],[0,0],[0,0]]]
#    return np.array(arr)
#array_zeros = func()
#print array_zeros

lst = [0] * 24

def array_zeros() :
    arr = np.array(lst)
    arr2 =arr.reshape(3,4,2)
    return arr2
array_zeros()
