# Default Imports
import numpy as np
path = "./data/ipl_matches_small.csv"

# Enter code here
def read_csv_data_to_ndarray(f_path, inp_dtype):
    n_array = np.genfromtxt(f_path,dtype=inp_dtype,delimiter=",",skip_header=1)
    return n_array
