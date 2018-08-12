# Default Imports
import numpy as np

# Enter solution here
def create_3d_array():
    #n = int(raw_input('Enter number of values to be stored in array : '))# number of elements inn array

    #calculate number of elemets that will be stored in 3D array = 3X3X3
    n = 3*3*3
    arr = np.arange(0,n)
    reshaped_arr = arr.reshape((3,3,3))
    #print arr
    #print reshaped_arr
    return reshaped_arr

#create_3d_array()
