# %load q04_read_csv_data_to_ndarray/build.py
# Default Imports
import numpy as np
path = './data/ipl_matches_small.csv'
dtypes = float

def read_csv_data_to_ndarray(path=path,dtypes=dtypes):
    ipl_array = np.genfromtxt(path, dtype=dtypes, skip_header=1, delimiter=',')
    return ipl_array



