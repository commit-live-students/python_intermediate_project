
import numpy as np
def get_total_extras():
    ipl = np.genfromtxt('data/ipl_matches_small.csv', dtype='|S20', skip_header=1, delimiter=',')
    ipl1 = ipl[0:2,17]
    sum_extras = np.sum(ipl[:,17].astype(np.int32))
    return sum_extras
get_total_extras()


