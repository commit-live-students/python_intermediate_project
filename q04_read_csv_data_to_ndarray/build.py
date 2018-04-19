# %load q04_read_csv_data_to_ndarray/build.py
# Default Imports
import numpy as np
path = './data/ipl_matches_small.csv'
dtype = '|S100'
def read_csv_data_to_ndarray(path,dtype):
    csvFileData = np.genfromtxt(path,skip_header=1,dtype=dtype,delimiter=',')
    print(csvFileData.shape)
    return csvFileData

read_csv_data_to_ndarray(path,dtype)

# Enter code here

