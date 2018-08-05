# %load q06_get_unique_matches_count/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np
path = 'data/ipl_matches_small.csv'


# Enter Code Here
def get_unique_matches_count():
    ipl_matches_array = np.genfromtxt('./data/ipl_matches_small.csv', dtype='|S50', delimiter=',', skip_header=1)
    unique_matches = np.unique(ipl_matches_array[:, 0])
    count = len(unique_matches)
    return count




