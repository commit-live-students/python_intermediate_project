# Default Imports
import numpy as np
path = "./data/ipl_matches_small.csv"

# Enter code here
def read_csv_data_to_ndarray(filePath,dtype=np.float64):

    return np.genfromtxt(filePath,dtype,delimiter=",", skip_header=1)
