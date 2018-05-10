# %load q05_read_csv_data/build.py
# Default imports
import numpy as np
path='data/ipl_matches_small.csv'
# Enter code here
def read_ipl_data_csv(path=path,dtype=float):
    return np.genfromtxt(path, dtype='|S50', skip_header=1, delimiter=',')
#print(read_ipl_data_csv().shape)
#print(read_ipl_data_csv().dtype)

