# %load q05_read_csv_data/build.py
# Default imports
import numpy as np
path = './data/ipl_matches_small.csv'
dtype = float
def read_ipl_data_csv(path,dtype):
    ipl_array = np.genfromtxt(path,dtype=dtype,skip_header=1,delimiter=',')
    return ipl_array


# Enter code here



