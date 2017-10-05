# Default Imports
import numpy as np
path = "./data/ipl_matches_small.csv"

def read_csv_data_to_ndarray(path, d_type = np.float64) :
    data = np.genfromtxt(path, dtype = d_type, skip_header=1, delimiter = ",")
    return data

read_csv_data_to_ndarray(path)
