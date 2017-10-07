# Default imports
import numpy as np

# Enter code here
def read_ipl_data_csv(path,dtype='|S50'):
    ipl_matches_array = np.genfromtxt(path,dtype=dtype,delimiter=',',skip_header=1)
    return ipl_matches_array

print read_ipl_data_csv('data/ipl_matches_small.csv',dtype='|S50')
