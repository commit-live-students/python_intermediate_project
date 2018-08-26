# %load q04_read_csv_data_to_ndarray/build.py
# Default Imports
import numpy as np
path = 'data/ipl_matches_small.csv'

# Enter code here
def read_csv_data_to_ndarray(path,d=np.float64):
    load_data=np.genfromtxt(path,delimiter=',',dtype=d,skip_header=1)
    return load_data;
print(read_csv_data_to_ndarray(path))


