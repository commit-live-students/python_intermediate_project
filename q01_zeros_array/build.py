# Default Imports
import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir),  '..'  ))
import numpy as np

# Your solution
def array_zeros():
    pcm = [
        [[0,0],
         [0,0],
         [0,0],
         [0,0]],
        [[0,0],
         [0,0],
         [0,0],
         [0,0]],
        [[0,0],
         [0,0],
         [0,0],
         [0,0]]
]
    zeros_array = np.array(pcm)
    return zeros_array
