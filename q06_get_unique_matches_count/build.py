# %load q06_get_unique_matches_count/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'
import numpy  as np
# Enter Code Here
def get_unique_matches_count():
    ipl_matches_array=read_ipl_data_csv(path,'|S100')
    ipl_matches_array=ipl_matches_array[:,0:1]
    return np.unique(ipl_matches_array).size



