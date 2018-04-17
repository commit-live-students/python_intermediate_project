# %load q07_get_unique_teams_set/build.py
# Default imports
import numpy as np
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'


def get_unique_teams_set():
    m = read_ipl_data_csv(path,'|S50')
    team1 = set(m[0:,3].astype(np.str))
    team2 = set(m[0:,4].astype(np.str))
    
    teams = team1.union(team2)
    
    return teams

