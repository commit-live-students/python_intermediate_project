# %load q05_read_csv_data/build.py
# Default imports
import numpy as np

# Enter code here
def read_ipl_data_csv(path,dtype):
    ipl_matches_array = np.genfromtxt(path,dtype=dtype,delimiter=',',skip_header=1)
    return ipl_matches_array



