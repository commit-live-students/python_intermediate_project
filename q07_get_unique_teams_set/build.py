# %load q07_get_unique_teams_set/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'
import numpy as np
import pandas as pd

def get_unique_teams_set():
    df=read_ipl_data_csv(path,dtype='|S50')
    return(set(np.unique(df[:,3])).union(np.unique(df[:,4])))
get_unique_teams_set()           


