# %load q06_get_unique_matches_count/build.py
# Default imports
import numpy as np
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'
def get_unique_matches_count():
    path = 'data/ipl_matches_small.csv'
    ipl_array = np.genfromtxt(path,delimiter = ',',skip_header = 1)
    #ipl_matches_array = ipl_array[:0]
    #return ipl_matches_array
    return np.unique(ipl_array[:,0]).size

get_unique_matches_count()
# Enter Code Here



