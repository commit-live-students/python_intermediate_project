# %load q04_read_csv_data_to_ndarray/build.py
# Default Imports
import numpy as np
path = './data/ipl_matches_small.csv'

def read_csv_data_to_ndarray(path,dtype):
    return np.genfromtxt(path,delimiter=',',dtype=dtype,skip_header=1)
    
    

# Enter code here
read_csv_data_to_ndarray('./data/ipl_matches_small.csv',int)


