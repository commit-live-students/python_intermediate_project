# Default Imports
import numpy as np
path = "./data/ipl_matches_small.csv"

# Enter code here
def read_csv_data_to_ndarray(path,dtype):
    data=np.genfromtxt(path,dtype=dtype,delimiter=",")[1:]
    return data
