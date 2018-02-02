# Default Imports
import numpy as np
import csv
path = "./data/ipl_matches_small.csv"

# Enter code here
def read_csv_data_to_ndarray(path, dtype=np.float64):
    narray = np.genfromtxt(path, dtype, delimiter=',', skip_header=1)
    #print narray
    return narray

#read_csv_data_to_ndarray(path, str)
