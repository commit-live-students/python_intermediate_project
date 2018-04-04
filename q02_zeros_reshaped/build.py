import numpy as np

def array_zeros():
    zeros_array = np.zeros((3, 4, 2))
    return zeros_array


# Default imports
import numpy as np
from greyatomlib.python_intermediate.q01_zeros_array.build import  array_zeros


def array_reshaped_zeros():
    ans = array_zeros()
    return ans.reshape(2,3,4)

