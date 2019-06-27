# %load q05_read_csv_data/build.py
# Default imports
import numpy as np

# Enter code here
path = './data/ipl_matches_small.csv'
dtype = '|S50'

def read_ipl_data_csv(path, dtype = '|S50'):
    ipl_matches_array = np.genfromtxt(path,dtype,delimiter=',', skip_header=1)
    #type(ipl_matches_array)
    #print (ipl_matches_array)
    return ipl_matches_array

read_ipl_data_csv(path, dtype)





