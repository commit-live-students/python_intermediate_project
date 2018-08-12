# Default Imports
import numpy as np
path = "./data/ipl_matches_small.csv"

def read_csv_data_to_ndarray(path,dtype='|S100'):
    ipl_array = np.genfromtxt(path,dtype = dtype,delimiter = ',',skip_header = 1)
    return ipl_array

# Enter code here
