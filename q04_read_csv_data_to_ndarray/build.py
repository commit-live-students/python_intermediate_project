# Default Imports
import numpy as np
path = "./data/ipl_matches_small.csv"

def read_csv_data_to_ndarray(path,dtype=np.float64):


    arr = np.genfromtxt(path,dtype=dtype,delimiter=",",skip_header=1)
    return arr
