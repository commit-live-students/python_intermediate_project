# %load q05_read_csv_data/build.py
# Default imports
import numpy as np
path='./data/ipl_matches_small.csv'

def read_ipl_data_csv(path,dtype='|S50'):
    ipl_matches_array = np.genfromtxt(path, skip_header=1, dtype=dtype, delimiter=',')
    return ipl_matches_array
read_ipl_data_csv(path)



