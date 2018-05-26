import numpy as np
def create_3d_array():
    
    array_3d = np.arange(0, 27, dtype=np.int32).reshape(3, 3, 3)
    return array_3d
testArray = create_3d_array()
print(testArray)

