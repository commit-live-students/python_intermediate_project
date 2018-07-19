# %load q01_zeros_array/build.py
# Default Imports
import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir),  '..'  ))
import numpy as np

# Your solution
def array_zeros():
    #return zero array
    zeros_array = np.random.randint(1,size=(3,4,2))
    return zeros_array


if __name__ == '__main__':
    array_zeros()
    print(array_zeros())


