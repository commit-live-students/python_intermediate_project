# Default Imports
import numpy as np
path = "./data/ipl_matches_small.csv"

# Enter code here
def read_csv_data_to_ndarray(path, dtype=np.float64):
    data = np.genfromtxt(path, delimiter=",", dtype=dtype, skip_header=1)
    return data
