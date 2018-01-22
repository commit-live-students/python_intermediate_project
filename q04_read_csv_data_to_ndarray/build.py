# Default Imports
import numpy as np
path = "./data/ipl_matches_small.csv"
input_dtype = '|S100'

def read_csv_data_to_ndarray(path,dtype):
    csv = np.genfromtxt(path,delimiter=",",skip_header=1,dtype=dtype)
    return csv

# Enter code here
