# Default imports
import numpy as np

# Enter code here

def read_ipl_data_csv(path, **kwargs) :
    data = np.genfromtxt(path, dtype = "|S50", skip_header = 0, delimiter = ",")
    ipl_matches_array = np.array(data)
    return ipl_matches_array

read_ipl_data_csv("./data/ipl_matches_small.csv")
