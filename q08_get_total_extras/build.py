import numpy as np
def get_total_extras():
    arr=np.genfromtxt('./data/ipl_matches_small.csv',delimiter=',',dtype=np.float64,skip_header=1)
    return(np.sum(arr[:,17]))

