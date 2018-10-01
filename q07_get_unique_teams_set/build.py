# %load q07_get_unique_teams_set/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'
import numpy as np
# Enter Code Here
def get_unique_teams_set(path=path,dtype=str):
    x=np.genfromtxt(path,delimiter=',',skip_header=1,dtype=None,usecols=3)
    y=np.genfromtxt(path,delimiter=',',skip_header=1,dtype=None,usecols=4)

    a=np.unique(x)
    b=np.unique(y)
    v=np.union1d(b,a)
    return set(v)














