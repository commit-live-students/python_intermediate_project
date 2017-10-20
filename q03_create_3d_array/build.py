# Default Imports
import numpy as np

# Enter solution here
def create_3d_array():
    numpy_3d_array = np.empty((3,3,3))
    #print(numpy_3d_array)
    temp_array = np.arange(0, (numpy_3d_array.size))
    numpy_3d_array = temp_array.reshape((3,3,3))
    return numpy_3d_array
    #print(temp_array)
    #print(numpy_3d_array)
#create_3d_array()
