# Default imports
import numpy as np

# Enter code here
dtype='|S20'
def read_ipl_data_csv(path, dtype):
    ipl_matches_array = np.genfromtxt(path, dtype=dtype, skip_header=1, delimiter=",")
    return ipl_matches_array
