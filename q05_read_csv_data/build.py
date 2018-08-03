# %load q05_read_csv_data/build.py
# Default imports
import numpy as np

# Enter code here
path = './data/ipl_matches_small.csv'
def read_ipl_data_csv(file_path, dtype):
    return np.genfromtxt(file_path, delimiter=',', dtype=dtype, skip_header=1)
read_ipl_data_csv(path,np.float64)



