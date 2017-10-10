# %load q05_read_csv_data/build.py
# Default imports
import numpy as np
import csv
path = "./data/ipl_matches_small.csv"

# Enter code here
def read_ipl_data_csv(path,dtype=np.float):

    ipl_matches_array=np.genfromtxt(path,dtype='|S50',skip_header=1,delimiter=",")
    #print(type(ipl_matches_array))
    return ipl_matches_array

read_ipl_data_csv(path)
# print(a.shape)
# print(a.dtype)
