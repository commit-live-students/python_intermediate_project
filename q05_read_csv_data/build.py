# %load q05_read_csv_data/build.py
# Default imports
import numpy as np

# Enter code here

from numpy import genfromtxt
path = 'data/ipl_matches_small.csv'

def read_ipl_data_csv(path,dtype = np.float64):
    ipl_matches_array=  np.genfromtxt(path,dtype='|S50',skip_header = 1 , delimiter = ',')
    return ipl_matches_array







