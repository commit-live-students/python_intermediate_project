# Default Imports
import numpy as np
from numpy import genfromtxt
path = "./data/ipl_matches_small.csv"

# Enter code here
def read_csv_data_to_ndarray(path, dtype):
    read_csv_data=genfromtxt(path,dtype, delimiter=',', skip_header=1)
    return(read_csv_data)
