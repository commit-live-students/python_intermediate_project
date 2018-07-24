# %load q04_read_csv_data_to_ndarray/build.py
# Default Imports

import numpy as np
path = './data/ipl_matches_small.csv'

def read_csv_data_to_ndarray(path, data_t = np.float64):
    ar = np.genfromtxt(path, delimiter=',', dtype=data_t, skip_header=1)
    return ar
 
    

# Enter code here



