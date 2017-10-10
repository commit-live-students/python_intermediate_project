# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = "data/ipl_matches_small.csv"

import numpy as np
from numpy import genfromtxt
# path = "./data/ipl_matches_small.csv"

# Enter code herefrom numpy import genfromtxt
def get_unique_teams_set() :
    ipl_matches_array = genfromtxt("./data/ipl_matches_small.csv", dtype = '|S20', delimiter=',', skip_header = 1)
    s1 = (ipl_matches_array[:,3])
    s2 = (ipl_matches_array[:,4])
    s3 = np.concatenate((s1, s2), axis=0)
    items, inv = np.unique(s3, return_inverse=True)

    #freq = np.bincount(inv)
    #np.array([items, freq]).T
    #np.array([items, freq]).T
    return set(items.flatten())

get_unique_teams_set()

# Enter Code Here
