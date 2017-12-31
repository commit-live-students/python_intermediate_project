# Default Imports
import numpy as np
path = "./data/ipl_matches_small.csv"

# Enter code here
def read_csv_data_to_ndarray(path,dtype=np.float64):
    with open(path,'r') as file:
        data = np.loadtxt(file, dtype=dtype,delimiter=',', skiprows=1)
        return np.asarray(data)
