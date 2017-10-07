# Default Imports
import numpy as np
path = "./data/ipl_matches_small.csv"

def read_csv_data_to_ndarray(filepath,input_dtype):
    return np.genfromtxt( filepath, dtype=input_dtype,skip_header=1,delimiter = ',')
