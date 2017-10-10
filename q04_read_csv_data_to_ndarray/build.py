# Default Imports
import numpy as np
path = "./data/ipl_matches_small.csv"

def read_csv_data_to_ndarray (path,dtype=np.float64):
    path1 = path
    dtype1 = dtype
    ipl = np.genfromtxt(path1,dtype=dtype1, skip_header=1,delimiter = ',')
    return ipl



read_csv_data_to_ndarray(path ,'|S50')
