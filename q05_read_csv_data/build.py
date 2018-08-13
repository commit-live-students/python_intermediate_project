# Default imports
import numpy as np
path = "./data/ipl_matches_small.csv"
# Enter code here
def read_ipl_data_csv(path, dtype=None):
    return np.genfromtxt(path, delimiter=',', dtype=dtype, skip_header=1)

ipl_matches_array = read_ipl_data_csv(path,'|S50')
