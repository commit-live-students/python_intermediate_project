# %load q04_read_csv_data_to_ndarray/build.py
# Default Imports
import numpy as np
path = './data/ipl_matches_small.csv'

from numpy import genfromtxt

# Enter code here
def read_csv_data_to_ndarray(path,str):
    return np.genfromtxt(path, delimiter=',',dtype=str,skip_header=1)


read_csv_data_to_ndarray(path,str)

