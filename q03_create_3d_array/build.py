# Default Imports
import numpy as np
def create_3d_array():
    value=np.zeros((3,3,3))
    elements=value.size
    total_values=np.arange(elements)
    reshape_array=total_values.reshape(3,3,3)
    return reshape_array
