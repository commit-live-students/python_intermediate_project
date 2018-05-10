# %load q07_get_unique_teams_set/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'
import numpy as np
import pandas as pd

# Enter Code Here
def get_unique_teams_set():
    l=read_ipl_data_csv(path,dtype='a')
    l=np.array(l)    
    #a=l[1:,4]
    #b=l[1:,3]
    c=np.union1d(l[1:,4],l[1:,3])
    return (c)

#print(get_unique_teams_set())




