# %load q07_get_unique_teams_set/build.py
# Default imports
import numpy as np
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_unique_teams_set():
    team_data=read_ipl_data_csv('./data/ipl_matches_small.csv','|S50')
    team1=np.unique(team_data[:,3])
    team2=np.unique(team_data[:,4])
    team_union=np.union1d(team1,team2)
    return set(team_union)

