# %load q05_read_csv_data/build.py
# Default imports
import numpy as np
path = "./data/ipl_matches_small.csv"

# Enter code here
def read_ipl_data_csv(path,dtype=None):
    ipl_matches_array=np.genfromtxt(path,delimiter=',',dtype='|S50',skip_header=1)
    return ipl_matches_array
print read_ipl_data_csv(path,dtype=None)
