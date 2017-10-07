# Default Imports
import numpy as np
path = "./data/ipl_matches_small.csv"

# Enter code here
def read_csv_data_to_ndarray(file_path, input_dtype):
    return np.genfromtxt(file_path, delimiter=',', dtype=input_dtype, skip_header=1)
