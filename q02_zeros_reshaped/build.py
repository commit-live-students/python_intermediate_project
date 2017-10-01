# Default imports

import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir), '..'))
import numpy as np
from q01_zeros_array.build import array_zeros

# Write your code
def array_reshaped_zeros():
    zeros_array_reshaped = array_zeros().reshape(2, 3, 4)
    return zeros_array_reshaped
