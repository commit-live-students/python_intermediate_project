# Default Imports
import numpy as np
path = "./data/ipl_matches_small.csv"
import csv
# Enter code here
def read_csv_data_to_ndarray(path, dtype=np.float64):
    file = np.genfromtxt(path, delimiter=',',skip_header=1,dtype=dtype)
    x=np.array(file)
    return x
