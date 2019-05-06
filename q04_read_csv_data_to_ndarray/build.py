# Default Imports
import numpy as np
path = './data/ipl_matches_small.csv'

def read_csv_data_to_ndarray(path, dtype=np.float64):
    return np.genfromtxt(path, dtype=dtype, skip_header=1, delimiter=',')

