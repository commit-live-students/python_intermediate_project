# %load q06_get_unique_matches_count/build.py
# Default imports
import numpy as np
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_unique_matches_count():
    ipl_matches_array = read_ipl_data_csv(path,'|S50')
    a = np.unique(ipl_matches_array[:,0],return_counts=True)
    p = list(a[1])
    return len(p)

get_unique_matches_count()

