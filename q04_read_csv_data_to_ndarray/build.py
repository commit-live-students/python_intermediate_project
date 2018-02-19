# %load q04_read_csv_data_to_ndarray/build.py
# Default Imports
import numpy as np
from io import BytesIO

path = './data/ipl_matches_small.csv'

# Enter code here

def read_csv_data_to_ndarray(path, dtype=np.float64):
    nd_array = np.genfromtxt(path, dtype=dtype, delimiter=',', skip_header=1)
    return nd_array


