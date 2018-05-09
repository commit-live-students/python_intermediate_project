# %load q07_get_unique_teams_set/build.py
# Default imports
import numpy as np
from numpy import genfromtxt
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_unique_teams_set():
    read_ipl_data_csv = np.genfromtxt(path,delimiter=',', dtype='str', skip_header=1)
    team1 = read_ipl_data_csv[: ,3]
    team2 = read_ipl_data_csv[: ,4]
    team1_u = np.unique(team1)
    team2_u = np.unique(team2)
    team_union = set(team1_u).union(set(team2_u))
    team_union_unique = np.unique(team_union)
    return team_union_unique
print(get_unique_teams_set())
def get_unique_teams_set():
    data = np.genfromtxt(path, dtype='str',delimiter = ',', skip_header = 1)
    team1 = data[:,3]
    team2 = data[:,4]
    unique1 = np.unique(team1)
    unique2 = np.unique(team2)
    union = set(unique1).union(set(unique2))
    return np.unique(union)
# Enter Code Here
print(get_unique_teams_set())

