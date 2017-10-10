import numpy as np
path = "./data/ipl_matches_small.csv"

def read_ipl_data_csv(path,dtype):
    ipl_matches_array = np.genfromtxt(path, dtype = '|S50',delimiter =",")
    return ipl_matches_array
