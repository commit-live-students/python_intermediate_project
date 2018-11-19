# %load q06_get_unique_matches_count/build.py
# Default imports
import numpy as np
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_unique_matches_count():
    ipl_matches_array = read_ipl_data_csv(path, dtype = '|S100')
    ipl_matches_array = np.unique(ipl_matches_array[1:,1])
    return len(ipl_matches_array)
get_unique_matches_count()


