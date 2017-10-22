# Default Imports
import numpy as np
path = "./data/ipl_matches_small.csv"

# Enter code here
def read_csv_data_to_ndarray(path, data_type=np.float64):
    data = np.genfromtxt(path, dtype = data_type, delimiter = ',', skip_header = 1)
    #print(data)
    return data
#read_csv_data_to_ndarray(path = './data/ipl_matches_small.csv')
