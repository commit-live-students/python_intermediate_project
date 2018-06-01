# %load q04_read_csv_data_to_ndarray/build.py
# Default Imports
import numpy as np
path = './data/ipl_matches_small.csv'
dtype = 'float64'
# Enter code here
def read_csv_data_to_ndarray(path,dtype):
    
    my_file = np.genfromtxt(path,dtype,skip_header=1,delimiter=',')
    return my_file

