# Default Imports
import numpy as np
path = "./data/ipl_matches_small.csv"

# Enter code here
import numpy as np
path = "./data/ipl_matches_small.csv"
def read_csv_data_to_ndarray(path, dtype=np.float64):
    ipl_data = np.genfromtxt(path, delimiter=",", dtype = dtype, skip_header = 1)

    return ipl_data
