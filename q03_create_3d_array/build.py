# %load q03_create_3d_array/build.py
# Default Imports
import numpy as np

def create_3d_array():
    number = np.random.randint(0,10, (3,3,3))
    count = np.size(number)
    number_array = np.arange(0,count)
    number_reshaped = number_array.reshape(3,3,3)
    return number_reshaped

# Enter solution here
