# %load q06_get_unique_matches_count/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

import numpy as np

def get_unique_matches_count():
    
    ipl_matches_array=np.genfromtxt(path, dtype='|S50',delimiter=',',skip_header=1)
    
    ipl_matches_array=len(np.unique(ipl_matches_array[:,0]))
    
    
    return ipl_matches_array


