#%load q05_read_csv_data/build.py

import numpy as np

path='./data/ipl_matches_small.csv'
dtype='|S50'

def read_ipl_data_csv(path,dtype):
    
    ipl_matches_array=np.genfromtxt(path,delimiter=',',skip_header=1,dtype=dtype)

#print(ipl_matches_array)
    return ipl_matches_array



