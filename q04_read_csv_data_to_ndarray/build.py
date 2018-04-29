# %load q04_read_csv_data_to_ndarray/build.py
# Default Imports
import numpy as np
path = './data/ipl_matches_small.csv'
dtypes= float
# Enter code here
def read_csv_data_to_ndarray(path=path,dtypes=dtypes):
    file_data=np.genfromtxt(path,dtype=dtypes , delimiter=',', skip_header=1)
    return file_data

