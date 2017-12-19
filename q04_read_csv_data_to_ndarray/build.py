# Default Imports
import numpy as np
path = "./data/ipl_matches_small.csv"
input_dtype = '|S100'

def read_csv_data_to_ndarray(path, input_dtype):
    ipl_array = np.genfromtxt(path,delimiter=',', dtype = input_dtype, skip_header= 1 )
    return ipl_array

ipl_array = read_csv_data_to_ndarray(path, input_dtype)
