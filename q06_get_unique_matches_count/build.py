# %load q06_get_unique_matches_count/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'
import numpy as np
# Enter Code Here
def get_unique_matches_count():
    a=np.genfromtxt('data/ipl_matches_small.csv',delimiter=',')
    b=np.unique(a[:,0])
    c=b[~np.isnan(b)]
    ipl_matches_array=np.prod(c.shape)
    return ipl_matches_array

c=get_unique_matches_count()
c


