# %load q05_read_csv_data/build.py
# Default imports
import numpy as np

path = './data/ipl_matches_small.csv'

def read_ipl_data_csv(path,dtype=np.float64):
    
    ipl_matches_array=array=np.genfromtxt(path, dtype='|S50',delimiter=',',skip_header=1)
    
    return ipl_matches_array

# Enter code here


