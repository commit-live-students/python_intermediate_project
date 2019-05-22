# Default Imports
import numpy as np
path = "./data/ipl_matches_small.csv"

def read_csv_data_to_ndarray(path = path, dtype = '|S100'):
    data = np.genfromtxt(path, delimiter=",", dtype = '|S100', skip_header = 1)
    return data
    return type(data)

read_csv_data_to_ndarray(path = path, dtype ='|S100' )
