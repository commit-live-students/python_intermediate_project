# Default Imports
import numpy as np

# Enter solution here

def create_3d_array ():
    zeros_array = np.zeros((3,3,3))
    values = zeros_array.size
    new_array = np.arange(values)
    final_array = new_array.reshape(3,3,3)
    return final_array
