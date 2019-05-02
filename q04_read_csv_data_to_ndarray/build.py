# %load q04_read_csv_data_to_ndarray/build.py
# Default Imports
import numpy as np
path = './data/ipl_matches_small.csv'

# Enter code here
def read_csv_data_to_ndarray(path, dtype = None):
    read_data = np.genfromtxt(path, dtype, delimiter = ',', skip_header = 1)
    return read_data

print read_csv_data_to_ndarray(path)
    


