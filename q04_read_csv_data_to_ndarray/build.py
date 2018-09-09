# %load q04_read_csv_data_to_ndarray/build.py
# Default Imports
import numpy as np
path = '../data/ipl_matches_small.csv'

def read_csv_data_to_ndarray(path,dtype = np.float64):
    load = np.genfromtxt(path,dtype =dtype, skip_header=1, delimiter=',')
    #load = np.array(load)
    return load
    
# Enter code here
#type(read_csv_data_to_ndarray('./data/ipl_matches_small.csv'))



