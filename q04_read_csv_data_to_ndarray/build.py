# Default Imports
import numpy as np
path = "./data/ipl_matches_small.csv"

# Enter code here
def read_csv_data_to_ndarray(path, dtype=np.float64):
    # path = "./data/ipl_matches_small.csv"
    marks = np.genfromtxt(path,skip_header=1,delimiter=',',dtype=dtype)
    return marks

# read_csv_data_to_ndarray(path,dtype)
