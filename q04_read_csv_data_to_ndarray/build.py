# Default Imports
import numpy as np
path = "./data/ipl_matches_small.csv"

def read_csv_data_to_ndarray():
    data = np.genfromtxt(path, delimiter=',')
    return type(data)
    return data

read_csv_data_to_ndarray()
