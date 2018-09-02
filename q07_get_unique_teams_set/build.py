# %load q07_get_unique_teams_set/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'
import numpy as np

# Enter Code Here
def get_unique_teams_set():
    read = np.genfromtxt(path,delimiter=',',dtype='|S50',skip_header=1)
    team1=set(np.unique(read[:,3]))
    team2=set(np.unique(read[:,4]))
    teams=team1.union(team2)
    return teams
    

print(get_unique_teams_set())


