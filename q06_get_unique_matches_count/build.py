# %load q06_get_unique_matches_count/build.py
# Default imports
import numpy as np
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

# Enter Code Here

def get_unique_matches_count():
    ipl_matches_array=np.genfromtxt(path,dtype='|S20',skip_header=1,delimiter=',')
    x=ipl_matches_array[:,4]
    y=ipl_matches_array[:,5]
    z=np.array(list(x)+list(y))
    return np.count_nonzero(np.unique(z))
get_unique_matches_count()


