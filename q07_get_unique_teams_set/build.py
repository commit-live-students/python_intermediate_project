# %load q07_get_unique_teams_set/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

import numpy as np

# Enter Code Here
def get_unique_teams_set():
    iplData = read_ipl_data_csv(path,'|S50')
    
    #print(iplData)
    #print(iplData[:,3])
    #print(iplData[:,4])
    #print(len(np.unique(iplData[:,3])))
    #print(len(np.unique(iplData[:,4])))
    team1 = np.unique(iplData[:,3])
    team2 = np.unique(iplData[:,4])
    #print(team1)
    #print(team2)
    allTeam = set(team1)
    team2Set = set(team2)
    allTeams = allTeam.union(team2Set)
    #print(allTeams)
    return allTeams
get_unique_teams_set()

