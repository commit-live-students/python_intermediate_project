# Default Imports
import numpy as np

def create_3d_array():
    numbers= list(range(0,27))
    my_array=np.array(numbers)
    my_array.resize((3,3,3))
    return my_array
