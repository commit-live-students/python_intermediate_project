# Default imports
import numpy as np

path = "./data/ipl_matches_small.csv"
dttype = '|S50'

def read_ipl_data_csv(path_par, dtype='|S50'):
    ipl_matches_array = np.genfromtxt(path_par, dtype=dtype, delimiter=",", skip_header=1)
    return ipl_matches_array

print read_ipl_data_csv(path, dtype='|S50')
