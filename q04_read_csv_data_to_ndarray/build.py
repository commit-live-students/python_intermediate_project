# %load q04_read_csv_data_to_ndarray/build.py
# Default Imports
import numpy as np
path = './data/ipl_matches_small.csv'

def read_csv_data_to_ndarray(path,dtype=type(float)):
    ipl_np = np.genfromtxt(path, dtype=dtype, skip_header=1, delimiter=',')
    return ipl_np

# Enter code here
print(read_csv_data_to_ndarray(path))


