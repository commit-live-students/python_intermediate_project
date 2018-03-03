# %load q07_get_unique_teams_set/build.py
# Default imports
import numpy as np
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_unique_teams_set():
    a = read_ipl_data_csv(path, dtype = '|S50')
    team1_uni = np.unique(a[:,3])
    team2_uni = np.unique(a[:,4])
    #print team1_uni
    #print team2_uni
    team_uni = set(np.union1d(team1_uni,team2_uni))
    return team_uni
    
get_unique_teams_set()

