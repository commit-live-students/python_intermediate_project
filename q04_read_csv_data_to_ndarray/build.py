# Default Imports
import numpy as np
path = "./data/ipl_matches_small.csv"
dtype = np.float64
# Enter code here
def read_csv_data_to_ndarray(path,dtype):
    data = np.genfromtxt(path, dtype, skip_header=1, delimiter=",")
    return data
# Enter code here

dt = read_csv_data_to_ndarray(path,dtype)
print dt
