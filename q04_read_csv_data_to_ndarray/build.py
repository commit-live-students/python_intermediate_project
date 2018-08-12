# Default Imports
import numpy as np
path = "./data/ipl_matches_small.csv"
def read_csv_data_to_ndarray(path , dtype = '|S100'):
    array = np.genfromtxt(path , delimiter=',', skip_header=1, dtype = '|S100')
    return array

print read_csv_data_to_ndarray(path)
