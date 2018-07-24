# %load q05_read_csv_data/build.py
# Default imports
import numpy as np

# Enter code here
path = './data/ipl_matches_small.csv'
data_type='|S50'


def read_ipl_data_csv(path,dtype):
    ipl_matches_array=np.genfromtxt(path,dtype=dtype,delimiter=',',skip_header=1)
    return ipl_matches_array

read_ipl_data_csv(path,data_type)


