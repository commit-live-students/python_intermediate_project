# Default imports
import numpy as np
path = "./data/ipl_matches_small.csv"
# Enter code here
def read_ipl_data_csv(path, dtype=np.float64):
    ipl_matches_array = np.genfromtxt(path, dtype, delimiter=",", skip_header=1)
    return ipl_matches_array
print read_ipl_data_csv(path)
