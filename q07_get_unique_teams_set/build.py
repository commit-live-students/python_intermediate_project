# %load q07_get_unique_teams_set/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'
import numpy as np
# Enter Code Here
def get_unique_teams_set():
    iplData = read_ipl_data_csv(path,'|S100')
    team1 = set(iplData[:,3].flatten())
    team2 = set(iplData[:,4].flatten()) 
    return team2.union(team1)




