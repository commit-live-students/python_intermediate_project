# %load q04_read_csv_data_to_ndarray/build.py
# Default Imports
import numpy as np

def read_csv_data_to_ndarray(path,dtype):
    #path = './data/ipl_matches_small.csv'
    return np.genfromtxt(path,delimiter=',',dtype=dtype,skip_header=1)

# Enter code here
cally=read_csv_data_to_ndarray('./data/ipl_matches_small.csv','|S20')
cally




