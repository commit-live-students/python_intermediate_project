# %load q06_get_unique_matches_count/build.py
# Default imports
import numpy as np
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'
dtype = '|S50'

# Enter Code Here
def get_unique_matches_count():
    ipl_array  = read_ipl_data_csv(path,dtype)
    ipl_matches_array = np.unique(ipl_array[:,0])
    return len(ipl_matches_array)


