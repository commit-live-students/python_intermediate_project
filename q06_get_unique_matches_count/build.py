# %load q06_get_unique_matches_count/build.py
# Default imports
import numpy as np
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_unique_matches_count():
    data = np.genfromtxt(path, dtype='|S100', skip_header=1, delimiter=',')
    match_code = data[:,0]
    match_code = set(match_code)
    ipl_matches_array = len(match_code)
    return ipl_matches_array
    
get_unique_matches_count()

