# %load q07_get_unique_teams_set/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np
# Enter Code Here

def get_unique_teams_set():
    whole_array = read_ipl_data_csv('data/ipl_matches_small.csv','|S25')
    team1 = np.unique(whole_array[:,3])
    team2 = np.unique(whole_array[:,4])
    unique_team = set(np.union1d(team1,team2))
    return unique_team


