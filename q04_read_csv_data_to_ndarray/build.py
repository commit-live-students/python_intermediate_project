# Default Imports
import numpy as np
path = "./data/ipl_matches_small.csv"

# Enter code here
def read_csv_data_to_ndarray(path,dtype=np.float64):
    f = np.genfromtxt(path, dtype = '|S50', skip_header = 1, delimiter = ",")
    print (f[0])
