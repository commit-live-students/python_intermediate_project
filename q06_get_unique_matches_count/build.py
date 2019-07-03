# %load q06_get_unique_matches_count/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np
path = 'data/ipl_matches_small.csv'
dtype = '|S100'
# Enter Code Here
def get_unique_matches_count():
    arr= read_ipl_data_csv(path,dtype)[:,0]
    arr1 = np.unique(arr)
    return arr1.size


