# %load q06_get_unique_matches_count/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'
import numpy as np
# Enter Code Here

data= np.genfromtxt(path, dtype='float', delimiter= ',', skip_header=1)

def get_unique_matches_count():
    matches_column= data[:,0]
    matches_unique = np.unique(matches_column)
    ipl_matches_array= matches_unique.size
    
    return ipl_matches_array
get_unique_matches_count()


