# Default imports
import numpy as np
path = "./data/ipl_matches_small.csv"

def read_ipl_data_csv(path,dtype):
    path1=path
    dtype1=dtype
    ipl_matches_array = np.genfromtxt(path1, dtype=dtype1, delimiter=",")

    return ipl_matches_array

read_ipl_data_csv(path,'|S50')

# Enter code here
