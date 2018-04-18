# %load q07_get_unique_teams_set/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'
import numpy as np
# Enter Code Here



def get_unique_teams_set():
    ipl_data = read_ipl_data_csv(path,'|S50')
    team1 = set(ipl_data[:,3])
    team2 = set(ipl_data[:,4])
    team1_union_team2 = team1.union(team2)
    return team1_union_team2
get_unique_teams_set()



