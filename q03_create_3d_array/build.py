# Default Imports
import numpy as np

# Enter solution here
def create_3d_array():
  ar1=np.zeros((3,3,3))
  N=ar1.size
  ar2=np.arange(N)
  ar3=ar2.reshape(3,3,3)
  return ar3
