# %load q07_get_unique_teams_set/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

# Enter Code Here
import numpy as np
def get_unique_teams_set():
    a=read_ipl_data_csv(path,dtype='|S50')
    b=set(a[:,3])
    c=set(a[:,4])
    return b.union(c)
    

c=get_unique_teams_set()
c


