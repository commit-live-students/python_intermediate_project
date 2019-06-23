# %load q05_read_csv_data/build.py
# Default imports
import numpy as np
# Enter code here
def read_ipl_data_csv(path,dtype='|S50'):
    dt=dtype
    ipl_matches_array=np.genfromtxt(path,delimiter=',',skip_header=1,dtype=dt)
    return ipl_matches_array
read_ipl_data_csv('data/ipl_matches_small.csv')


