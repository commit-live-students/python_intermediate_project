# Default Imports
import numpy as np
from numpy import genfromtxt
path = "./data/ipl_matches_small.csv"

# Enter code herefrom numpy import genfromtxt
def read_csv_data_to_ndarray(path, dtype = np.float64) :
    my_data = genfromtxt(path, delimiter=',', dtype=dtype, skip_header = 1)
    return my_data
