# %load q07_get_unique_teams_set/build.py
# Default imports
import numpy as np
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv


# Enter Code Here
def get_unique_teams_set():
    path = 'data/ipl_matches_small.csv'
    ipl_data = read_ipl_data_csv(path,'|S50')
    team1 = np.unique(ipl_data[:,3])
    team2 = np.unique(ipl_data[:,4])
    total_teams = np.union1d(team1,team2)
    return set(np.unique(total_teams))

get_unique_teams_set()
def get_unique_teams_set():
    path = 'data/ipl_matches_small.csv'
    ipl_data = read_ipl_data_csv(path,'|S50')
    team1 = np.unique(ipl_data[:,3])
    team2 = np.unique(ipl_data[:,4])
    total_teams = np.union1d(team1,team2)
    return set(np.unique(total_teams))

get_unique_teams_set()


