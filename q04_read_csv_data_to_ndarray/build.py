# %load q04_read_csv_data_to_ndarray/build.py
# Default Imports
import numpy as np
path = './data/ipl_matches_small.csv'
dtype = np.float64
# Enter code here
def read_csv_data_to_ndarray(path,dtype):
    ipl = np.genfromtxt(path,dtype,skip_header=1,delimiter=',')
    return ipl
read_csv_data_to_ndarray(path,dtype)

