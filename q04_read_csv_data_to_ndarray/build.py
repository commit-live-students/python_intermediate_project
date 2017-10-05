# %load q04_read_csv_data_to_ndarray/build.py
# Default Imports
import numpy as np
path = "./data/ipl_matches_small.csv"

# Enter code here
def read_csv_data_to_ndarray(path,dtype=np.float64):
    nparray=np.genfromtxt(path,dtype=dtype, skip_header=1,delimiter=",")
    return nparray
#npar=read_csv_data_to_ndarray(path)
#print(npar)
