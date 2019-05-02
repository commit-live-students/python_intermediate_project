# %load q06_get_unique_matches_count/build.py

# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np
from numpy import genfromtxt
path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_unique_matches_count():
    read_data = read_ipl_data_csv(path, dtype = '|S50')
    match = read_data[:,0]
    ipl_matches_array = np.unique(match)
    return len(ipl_matches_array)

print get_unique_matches_count()


