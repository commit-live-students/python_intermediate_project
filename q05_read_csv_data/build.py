# %load q05_read_csv_data/build.py
# Default imports
import numpy as np

path = './data/ipl_matches_small.csv'
dtype = float

def read_ipl_data_csv(path=path,dtype=dtype):
    ipl_matches_array = np.genfromtxt(path, dtype='|S50', skip_header=1, delimiter=',')
    return ipl_matches_array



