# %load q07_get_unique_teams_set/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_unique_teams_set():
    data = read_ipl_data_csv(path, dtype = '|S50')
    data1 = data[:,3]
    team1 = np.unique(data1)
    data2 = data[:,4]
    team2 = np.unique(data2)
    teams_played = np.union1d(team1, team2)
    return set(teams_played)

get_unique_teams_set()



