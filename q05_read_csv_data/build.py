# Default imports
import numpy as np

# Enter code here

def read_ipl_data_csv(path = "./data/ipl_matches_small.csv", dtype = np.float64):
    ipl_matches_array = np.genfromtxt(path, delimiter = ',', dtype = '|S50', skip_header = 1)
    return ipl_matches_array
