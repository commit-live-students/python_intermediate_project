# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'
import numpy as np
# Enter Code Here
dtype='|S20'
def get_unique_matches_count():
     data=np.genfromtxt("data/ipl_matches_small.csv", skip_header=1,delimiter=",", dtype=np.int64);
     match_code = data[:,0]
     bincount = np.bincount(match_code)
     ipl_matches_array = np.count_nonzero(bincount)
     return ipl_matches_array
