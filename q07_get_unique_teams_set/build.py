# %load q07_get_unique_teams_set/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'
import numpy as np

# get unique team values and union it
def get_unique_teams_set():
    data = read_ipl_data_csv(path,'|S30')
    team1 = data[:,3]
    team2 = data[:,4]
    unique_teams = set(np.append(team1,team2))
    return unique_teams

get_unique_teams_set()
print(get_unique_teams_set())


