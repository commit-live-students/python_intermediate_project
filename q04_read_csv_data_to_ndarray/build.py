# Default Imports
import numpy as np
path = "./data/ipl_matches_small.csv"

def read_csv_data_to_ndarray(path=path,dtype=np.float64):
    my_data = np.genfromtxt(path, delimiter=',',skip_header=1,dtype=dtype)
    return my_data
