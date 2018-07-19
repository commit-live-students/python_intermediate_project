# %load q06_get_unique_matches_count/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

# Enter Code Here
import numpy as np
def get_unique_matches_count():
    data=np.genfromtxt(path,delimiter=',',dtype='|S50',skip_header=1)
    ipl_matches_array=len(np.unique(data[:,0]))
    return ipl_matches_array



