# %load q04_read_csv_data_to_ndarray/build.py
# Default Imports
import numpy as np

# Enter code here
def read_csv_data_to_ndarray():
    path = './data/ipl_matches_small.csv'
    a = np.genfromtxt(path,delimiter=',',skip_header=1,dtype=s)
    return a 


