# Default Imports
import numpy as np
path = "./data/ipl_matches_small.csv"

# Enter code here
def read_csv_data_to_ndarray(path, dtype=np.float64):
    a = np.genfromtxt(path,delimiter=',',dtype=dtype)
    b = np.delete(a,0,0)
    print b.shape
    return b
