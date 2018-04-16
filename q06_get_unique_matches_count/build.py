# %load q06_get_unique_matches_count/build.py
# Default imports
import numpy as np
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'
# Enter Code Here
def get_unique_matches_count():
    m = np.genfromtxt(path,dtype='|S50',skip_header=1,delimiter=',')
    match_code = m[0:,0].astype(np.int64)
    ipl_match_array = len(set(match_code))
    
    return ipl_match_array


