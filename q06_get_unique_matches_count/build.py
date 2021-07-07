
import numpy as np
def get_unique_matches_count():
    ipl = np.genfromtxt('data/ipl_matches_small.csv', dtype='|S20', skip_header=1, delimiter=',')
    ipl_matches_array = np.unique(ipl[:,0])
    return len(ipl_matches_array)
get_unique_matches_count()


