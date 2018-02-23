# Default Imports
import numpy as np
path = "./data/ipl_matches_small.csv"

# Enter code here
dtype = np.float64
def read_csv_data_to_ndarray(path,dtype):
    array = np.genfromtxt(path, dtype=dtype, skip_header=1, delimiter=",")
    return array

print (read_csv_data_to_ndarray(path,dtype))
