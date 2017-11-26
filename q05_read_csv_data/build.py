# Default imports
import numpy as np

# Enter code here
def read_ipl_data_csv(path,dtype=np.float64):
    ipl_matches_array=np.genfromtxt(path,dtype=dtype,delimiter=',',skip_header=1)
    return ipl_matches_array

read_ipl_data_csv(path='data/ipl_matches_small.csv',dtype='S50')
