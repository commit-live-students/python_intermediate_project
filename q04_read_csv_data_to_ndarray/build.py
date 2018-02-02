# Default Imports
import numpy as np
path = "./data/ipl_matches_small.csv"

# Enter code here
def read_csv_data_to_ndarray(path, dtype = np.float64):
    ipl = np.genfromtxt(path, dtype, skip_header=1, delimiter=",")

    return ipl

read_csv_data_to_ndarray(path)
