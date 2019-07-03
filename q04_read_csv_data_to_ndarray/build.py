# %load q04_read_csv_data_to_ndarray/build.py
# Default Imports
import numpy as np

path = './data/ipl_matches_small.csv'

def read_csv_data_to_ndarray(path,dtype=type(float)):
    ipl_np=np.genfromtxt(path, delimiter=',',skip_header=1,dtype=dtype)
    return ipl_np

print(read_csv_data_to_ndarray(path))
    

# Enter code here


