# Default imports
import numpy as np

# Enter code here
path0 = "./data/ipl_matches_small.csv"

def read_ipl_data_csv(path, dtype = "|S50") :
    data = np.genfromtxt(path, dtype = "|S50", skip_header = 1, delimiter = ",")
    ipl_matches_array = np.array(data)
    return ipl_matches_array

read_ipl_data_csv(path0)
