# %load q04_read_csv_data_to_ndarray/build.py
# Default Imports
import numpy as np
import csv
import os


 
path = 'data/ipl_matches_small.csv'
dtype = '|S100'

def read_csv_data_to_ndarray(path,dtype):
    arr1= np.genfromtxt(path,delimiter=',',dtype='|S100',skip_header=1)
    return arr1

read_csv_data_to_ndarray(path,dtype)

# print(os.getcwd())

# Enter code here


