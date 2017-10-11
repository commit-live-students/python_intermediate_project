# Default Imports
import numpy as np
path = "./data/ipl_matches_small.csv"

# Enter code here
def read_csv_data_to_ndarray(path, dtype='float64'):
    with open(path) as csv:
        data = np.genfromtxt(path, dtype=dtype, skip_header=1, delimiter = ',')
    return data
