# %load q05_read_csv_data/build.py
# Default imports
import numpy as np

# Enter code here
def read_ipl_data_csv(path='./data/ipl_matches_small.csv', dtype=np.float):
    ipl_matches_array=np.genfromtxt(path,dtype='|S50', skip_header=1, delimiter=',')
    return ipl_matches_array

