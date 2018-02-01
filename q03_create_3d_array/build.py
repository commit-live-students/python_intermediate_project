# Default Imports
import numpy as np

# Enter solution here
def creat_3d_array():
    array = np.empty([3,3,3])
    N = array.size

    a = []

    for i in range(N):
        a.append(i)

    b = np.reshape(a, (3,3,3))

    return b
