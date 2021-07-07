# %load q06_get_unique_matches_count/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = './data/ipl_matches_small.csv'
import numpy as np
# Enter Code Here

def get_unique_matches_count(path=path,dtype=int):
    x=np.genfromtxt(path,dtype=dtype,delimiter=',',skip_header=1)
    #ipl_matches_array = []
    ipl_matches_array = len( np.unique(x[:,0]))
    return ipl_matches_array






get_unique_matches_count('./data/ipl_matches_small.csv',int)






