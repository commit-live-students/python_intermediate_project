# %load q05_read_csv_data/build.py
# Default imports
import numpy as np

path = './data/ipl_matches_small.csv'
dtype='|S50'

def read_ipl_data_csv(path,dtype):
    return np.genfromtxt(path,dtype,skip_header=1,delimiter=',')
