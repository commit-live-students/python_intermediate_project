# Default imports
import numpy as np

# Enter code here
def read_ipl_data_csv(path,dtype=None):
    ipl_matches_array=np.genfromtxt(path,delimiter=',',dtype=dtype,skip_header=True)
    return ipl_matches_array
