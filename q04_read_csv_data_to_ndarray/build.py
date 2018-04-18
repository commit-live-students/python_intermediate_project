# Default Imports
import csv
import numpy as np
path = "./data/ipl_matches_small.csv"

# Enter code here
def read_csv_data_to_ndarray(path,dtype=np.float64):
    a=np.genfromtxt(path,dtype,delimiter=',',skip_header=1)
    return a
#print(read_csv_data_to_ndarray(path))
