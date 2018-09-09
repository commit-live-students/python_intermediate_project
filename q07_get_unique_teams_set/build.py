# %load q07_get_unique_teams_set/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'
import numpy as np
# Enter Code Here
def get_unique_teams_set():
    team1 = np.unique(read_ipl_data_csv('data/ipl_matches_small.csv','S50')[:,3])
    team2 = np.unique(read_ipl_data_csv('data/ipl_matches_small.csv','S50')[:,4])
    all_teams = set(np.unique(np.concatenate((team1,team2),axis=0)))
    
    return all_teams
    

#get_unique_teams_set()


