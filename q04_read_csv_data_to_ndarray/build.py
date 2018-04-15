# %load q04_read_csv_data_to_ndarray/build.py
# Default Imports
import numpy as np
path = './data/ipl_matches_small.csv'
dtype1=np.float64
# Enter code here
def read_csv_data_to_ndarray(path=path,dtype1=dtype1):
    arr_csv=np.genfromtxt(path,dtype=dtype1, skip_header=1, delimiter=',')
    return arr_csv

