# %load q02_zeros_reshaped/build.py
# Default imports
import numpy as np
from greyatomlib.python_intermediate.q01_zeros_array.build import  array_zeros

# Write your code
def array_reshaped_zeros():
    main_arr = np.zeros((3,4,2))
    sec_arr = np.reshape(main_arr,(2,3,4))
    return sec_arr
array_reshaped_zeros()


