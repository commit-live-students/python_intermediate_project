# Default imports
import numpy as np
path = "./data/ipl_matches_small.csv"
def read_ipl_data_csv(path , dtype = float):
    ipl_matches_array = np.genfromtxt(path , delimiter=',',skip_header=1, dtype='|S50')
    return ipl_matches_array

print read_ipl_data_csv(path , dtype= float)
