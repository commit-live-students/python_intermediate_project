# Default Imports
import numpy as np
# Enter solution here
def create_3d_array():
    empty_array = np.zeros((3,3,3))
    total_values = empty_array.size
    new_array = np.arange(total_values)
    final_array = new_array.reshape(3,3,3)
    return final_array
