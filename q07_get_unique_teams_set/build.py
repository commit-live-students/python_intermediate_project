# %load q07_get_unique_teams_set/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'
import numpy as np

# Enter Code Here
def get_unique_teams_set():
    x=np.genfromtxt(path,dtype=str,delimiter=',',skip_header=1,usecols=3)
    y=np.genfromtxt(path,dtype=str,delimiter=',',skip_header=1,usecols=4)
    
    a=np.unique(x)
    b=np.unique(y)
    v=np.union1d(b,a)
    return set(v)
get_unique_teams_set()
set() 


