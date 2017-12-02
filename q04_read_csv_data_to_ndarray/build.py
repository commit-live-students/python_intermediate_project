# Default Imports
import numpy as np
path = "./data/ipl_matches_small.csv"

# Enter code heredef read_csv_data_to_ndarray(path,input_dtype=None):
    # Enter code here
def read_csv_data_to_ndarray(path,input_dtype=None):
    txt_array=np.genfromtxt(path,delimiter=',',dtype='S100',skip_header=True)
    return txt_array
