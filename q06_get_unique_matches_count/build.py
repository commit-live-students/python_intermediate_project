import numpy as np
def get_unique_matches_count():
    arr=np.genfromtxt('./data/ipl_matches_small.csv',delimiter=',',dtype='|S50',skip_header=1)
    ipl_matches_array=len(np.unique(arr[:,0]))
    return ipl_matches_array

