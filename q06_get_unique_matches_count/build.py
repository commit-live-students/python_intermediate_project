# %load q06_get_unique_matches_count/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np
path = 'data/ipl_matches_small.csv'

# Enter Code Here

def get_unique_matches_count():
    ipl_matches_array=len(set(np.genfromtxt(path,dtype='|S20',delimiter=',',skip_header=1)[:,0]))
    return ipl_matches_array

get_unique_matches_count()

open('data/ipl_matches_small.csv','r').read()


