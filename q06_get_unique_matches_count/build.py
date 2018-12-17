# Default imports
import numpy as np
path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_unique_matches_count():
    arr = np.genfromtxt(path,dtype='|S100', skip_header=1, delimiter=',')
    return len(set(arr[:,0]))



