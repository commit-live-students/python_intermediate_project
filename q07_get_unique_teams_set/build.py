# %load q07_get_unique_teams_set/build.py
# Default imports
import numpy as np
import pandas as pd

from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'
dtype = '|S50'

def get_unique_teams_set():
    ipl_matches = read_ipl_data_csv(path, dtype)
    ipl_match_team1 = ipl_matches[:,3]
    a = set(ipl_match_team1)
    
    ipl_match_team2 = ipl_matches[:,4]
    b = set(ipl_match_team2)
    
    return a.union(b)




