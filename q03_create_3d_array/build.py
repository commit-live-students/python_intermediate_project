# %load q03_create_3d_array/build.py
# Default Imports

# Enter solution here
import numpy as np

def create_3d_array():
    N = 3*3*3
    
    numbers = []
    for x in range(0,N):
        numbers.append(x)
        
    array_number = np.array(numbers)
    array_number = array_number.reshape(3,3,3)
    
    return array_number




