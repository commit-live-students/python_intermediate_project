# %load q04_read_csv_data_to_ndarray/build.py
# Default Imports
import numpy as np
path = './data/ipl_matches_small.csv'

# Enter code here
def read_csv_data_to_ndarray(path=path,d=np.float64):
    f=np.genfromtxt(path,delimiter=',',skip_header=1,dtype=d)
    return f


