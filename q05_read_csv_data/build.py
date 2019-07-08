# %load q05_read_csv_data/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv

import numpy as np

# Enter code here
def read_ipl_data_csv(a,dtype='|S50'):
    dt=dtype
    ipl_matches_array=np.genfromtxt(a,delimiter=',',skip_header=1,dtype=dt)
    return ipl_matches_array
path ='data/ipl_matches_small.csv'
d=read_ipl_data_csv(path)


d





