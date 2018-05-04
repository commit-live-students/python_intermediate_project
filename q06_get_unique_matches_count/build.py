# %load q06_get_unique_matches_count/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np
path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_unique_matches_count():
    ipl_matches_array = read_ipl_data_csv('data/ipl_matches_small.csv',
                                          dtype='|S50')
    return len(set(ipl_matches_array[:, 0]))

    

ipl_matches_array = read_ipl_data_csv('data/ipl_matches_small.csv',
                                          dtype='|S50')
def get_unique_matches_count():
    data=np.genfromtxt(path,delimiter=',',skip_header=1)
    xxx = len(np.unique(data[0]))
    return xxx
get_unique_matches_count()
len(np.unique(data[:,0])),data.shape
1451/20/6

len(set(ipl_matches_array[:, 0]))


