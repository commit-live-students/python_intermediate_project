# %load q05_read_csv_data/build.py
# Default imports

import numpy as np

path = './data/ipl_matches_small.csv'

def read_ipl_data_csv(path, dtype=np.float64):
    
    arr = np.genfromtxt(path, delimiter=',', dtype = dtype , skip_header=1)
    ipl_matches_array = arr[:,:].astype('|S50')
    print(type(ipl_matches_array))
    return ipl_matches_array

read_ipl_data_csv(path, dtype=np.float64)






