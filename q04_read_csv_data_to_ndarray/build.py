# Default Imports
import numpy as np
path = "./data/ipl_matches_small.csv"

# Enter code here
def read_csv_data_to_ndarray(path,input_dtype):
    ipl_match = np.genfromtxt(path,dtype = input_dtype,skip_header = 1, delimiter=",")
    return ipl_match
