# %load q07_get_unique_teams_set/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np
path = 'data/ipl_matches_small.csv'

def get_unique_teams_set():
    arr = read_ipl_data_csv(path,'|S100')
    team1,team2 = arr[:,3],arr[:,4]
    return set.union(set(team1),set(team2))

# Enter Code Here
get_unique_teams_set()



