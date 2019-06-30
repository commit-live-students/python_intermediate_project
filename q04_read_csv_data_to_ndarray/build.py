# %load q04_read_csv_data_to_ndarray/build.py
# Default Imports
import numpy as np
path = './data/ipl_matches_small.csv'
data_type='float64'
# Enter code here

def read_csv_data_to_ndarray(path,d):
    
    ipl=np.genfromtxt(path,dtype='|S100',delimiter=',',skip_header=1)
    return ipl

read_csv_data_to_ndarray(path,data_type)

    



