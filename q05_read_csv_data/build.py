# Default imports
import numpy as np

# Enter code here
path = "./data/ipl_matches_small.csv"
def read_ipl_data_csv(path, dtype):
    ipl_matches_array = np.genfromtxt(path , delimiter=',',skip_header=1, dtype=dtype)
    return ipl_matches_array

print read_ipl_data_csv(path, dtype='|S50')

     
