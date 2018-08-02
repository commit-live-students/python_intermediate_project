# %load q07_get_unique_teams_set/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

import numpy as np
def get_unique_teams_set():
    match = read_ipl_data_csv(path,'|S50')
    team1 = match[:, 3]
    team2 = match[:, 4]
    team=np.union1d( team1,team2 )
    fteam=set(team)
    return fteam
   




