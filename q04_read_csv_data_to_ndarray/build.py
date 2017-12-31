# Default Imports
import numpy as np
path = "./data/ipl_matches_small.csv"

def read_csv_data_to_ndarray(path,dtype):
    second =np.genfromtxt(path,delimiter=',',dtype=dtype,skip_header=1)
    return second

read_csv_data_to_ndarray(path,np.float64)
# Enter code here
