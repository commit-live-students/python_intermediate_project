# %load q04_read_csv_data_to_ndarray/build.py
# Default Imports
import numpy as np
import csv
path = './data/ipl_matches_small.csv'



def read_csv_data_to_ndarray(path,datatype=np.float64):
    data = np.genfromtxt(path, dtype=datatype,delimiter=',', skip_header=1)
    return data

