# Default Imports
import numpy as np

# Enter solution here
def create_3d_array():
    #initialize an empty array of (3,3,3) dimension
    numpy_3d_array = np.empty((3,3,3))
    #create an array using np.arange of size N i.e size of (3,3,3) np array
    temp_array = np.arange(0, (numpy_3d_array.size))
    #reshape the array using .reshape
    numpy_3d_array = temp_array.reshape((3,3,3))
    return numpy_3d_array
