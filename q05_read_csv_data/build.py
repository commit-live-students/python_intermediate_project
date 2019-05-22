# Default Imports
import numpy as np
path = "./data/ipl_matches_small.csv"

def read_ipl_data_csv(path = path, dtype='|S50'):
    ipl_matches_array = np.genfromtxt(path, delimiter=",", dtype='|S50', skip_header = 1)
    return ipl_matches_array

read_ipl_data_csv(path = path, dtype='|S50' )
