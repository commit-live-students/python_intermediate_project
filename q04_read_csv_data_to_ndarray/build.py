# %load q04_read_csv_data_to_ndarray/build.py
# Default Imports
import numpy as np
import csv
path = "./data/ipl_matches_small.csv"

# Enter code here
def read_csv_data_to_ndarray(path,dtype=np.float64):
    numpy_array=np.genfromtxt(path,dtype='|S100', skip_header=1, delimiter=",")


    return numpy_array

read_csv_data_to_ndarray(path)

# print(a.shape)
# print(a.dtype)
# print(a.shape == (1451, 23))
# print(a.dtype == '|S100')
