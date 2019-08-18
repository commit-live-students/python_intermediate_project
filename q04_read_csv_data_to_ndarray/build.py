# Default Imports
import numpy as np
path = "./data/ipl_matches_small.csv"

# Enter code here

def read_csv_data_to_ndarray(path, input_dtype):
    iplarray = np.genfromtxt(path,input_dtype, delimiter=',', skip_header = 1)
    return iplarray
