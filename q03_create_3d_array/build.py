import numpy as np
def create_3d_array() :
    array=np.array(range(0,27))
    size=array.size
    array_reshaped=array.reshape(3,3,3)
    return array_reshaped

