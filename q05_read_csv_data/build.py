# %load q05_read_csv_data/build.py
# Default imports
import numpy as np

path='./data/ipl_matches_small.csv'
dtype1=np.float64
# Enter code here
def read_ipl_data_csv(path=path,dtype1=dtype1):
    ipl_matches_array=np.genfromtxt(path,dtype='|S50', skip_header=1, delimiter=',')
    return ipl_matches_array

