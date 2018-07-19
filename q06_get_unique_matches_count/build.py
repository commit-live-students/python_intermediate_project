# %load q06_get_unique_matches_count/build.py
# Default imports 
import numpy as np
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'


def get_unique_matches_count():
    ipl_match_array = read_ipl_data_csv(path,'|S50')
    matches = len(np.unique(ipl_match_array[:,0]))
    return matches

print(get_unique_matches_count())



