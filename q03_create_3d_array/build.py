# Default Imports
import numpy as np

# Enter solution here
def create_3d_array():
    ary = np.empty([3,3,3])
    N = ary.size

    a = []

    for i in range(N):
        a.append(i)

    b = np.reshape(a, (3,3,3))

    return b
