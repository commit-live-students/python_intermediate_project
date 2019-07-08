# %load q04_read_csv_data_to_ndarray/build.py
# Default Imports
import numpy as np
# Enter code here
def read_csv_data_to_ndarray(a,b):
    ar=np.genfromtxt(a,delimiter=',',skip_header=1,dtype=b)
    return ar
path = './data/ipl_matches_small.csv'
db=float
c=read_csv_data_to_ndarray(path,db)







