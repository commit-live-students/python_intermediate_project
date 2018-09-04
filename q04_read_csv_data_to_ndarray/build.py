# %load q04_read_csv_data_to_ndarray/build.py
# Default Imports
import numpy as np
path = './data/ipl_matches_small.csv'
dtype ='|S20'
def read_csv_data_to_ndarray(path,dtype):
    ipl_array=np.genfromtxt(path,dtype,skip_header=1,delimiter=',')
    return ipl_array 
# Enter code here


