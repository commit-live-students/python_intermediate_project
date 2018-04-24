# %load q07_get_unique_teams_set/build.py
# Default imports
import numpy as np
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_unique_teams_set():
    ipl_matches_array =  read_ipl_data_csv(path,'|S20')
    team1 = ipl_matches_array[:,3].astype(np.object)
    team1 = np.unique(team1)    
#     print(team1)
    team2 = ipl_matches_array[:,4].astype(np.object)
    team2 = np.unique(team2)
#     print(team2)
    teams = np.union1d(team1,team2)
#     print(teams)
    teams = np.unique(teams)
    return teams 
#     
    
get_unique_teams_set()

