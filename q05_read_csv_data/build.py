# Default imports
import numpy as np

# Enter code here
def read_ipl_data_csv(path,dtype=np.float64):
    ipl_matches_array = np.genfromtxt(path,dtype, skip_header=1, delimiter=",")
    return ipl_matches_array
