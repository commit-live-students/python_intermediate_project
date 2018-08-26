# %load q05_read_csv_data/build.py
# Default imports
import numpy as np

def read_ipl_data_csv(path, dtype=np.float64):
    ipl_matches_array = np.genfromtxt(path, delimiter=',',dtype=dtype, skip_header=1)
    return ipl_matches_array

read_ipl_data_csv('./data/ipl_matches_small.csv','|S50')


