# Default imports
import numpy as np
path = "./data/ipl_matches_small.csv"
# Enter code here
def read_ipl_data_csv(path,dtype):
    dt=dtype
    ipl_matches_array= np.genfromtxt(path,delimiter=',',dtype='|S50',skip_header=1)
    
    return ipl_matches_array
