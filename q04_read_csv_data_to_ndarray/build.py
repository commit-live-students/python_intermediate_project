# Default Imports
import numpy as np
path = "./data/ipl_matches_small.csv"

def read_csv_data_to_ndarray(path, in_dtype):
    with open(path, 'r') as stream:
        out_array = np.genfromtxt(stream, skip_header=1, delimiter=',', dtype=in_dtype)

    return out_array
