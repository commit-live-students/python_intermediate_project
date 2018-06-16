# %load q07_get_unique_teams_set/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'
import numpy as np
# Enter Code Here
def get_unique_teams_set():
    team1 =np.genfromtxt(path, delimiter=',',dtype=str)[1:,[3]]
    team2=np.genfromtxt(path, delimiter=',',dtype=str)[1:,[4]]
    team1=np.unique(team1)
    team2=np.unique(team2)
    return np.union1d(team1,team2)

get_unique_teams_set()




