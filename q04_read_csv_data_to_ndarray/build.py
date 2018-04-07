# Default Imports
import numpy as np
path = "./data/ipl_matches_small.csv"

# Enter code here
dtype='float64'
def read_csv_data_to_ndarray(path,dtype):
    data= np.genfromtxt(path, skip_header=1,delimiter=",",dtype=dtype);
    return data
