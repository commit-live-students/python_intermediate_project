# %load q06_get_unique_matches_count/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_unique_matches_count():
    ipl_matches_array = read_ipl_data_csv(path, 'U25')
    ipl_matches_array = ipl_matches_array[:,0]
    count = len(np.unique(ipl_matches_array, axis=0))
    return count
import numpy as np
np.set_printoptions(threshold=np.inf)
get_unique_matches_count()


