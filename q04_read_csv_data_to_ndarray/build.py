# Default Imports
import numpy as np
path = "./data/ipl_matches_small.csv"

# Enter code here
def read_csv_data_to_ndarray(path,dtype=np.float):
    narray = np.genfromtxt(path, dtype='|S100', skip_header=1, delimiter=",")
    return narray
