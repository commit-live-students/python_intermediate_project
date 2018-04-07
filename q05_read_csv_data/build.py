# Default imports
import numpy as np

# Enter code here
dtype='|S50'
def read_ipl_data_csv(path, dtype):
    ipl_matches_array = np.genfromtxt(path, skip_header=1,delimiter=",",dtype=dtype)
    return ipl_matches_array
