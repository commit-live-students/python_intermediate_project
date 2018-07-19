# %load q07_get_unique_teams_set/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

# Enter Code Here
import numpy as np
def get_unique_teams_set():
    data=np.genfromtxt(path,delimiter=',',dtype='|S50',skip_header=1)
    team1=set(np.unique(data[:,3]))
    team2=set(np.unique(data[:,4]))
    teams=team1.union(team2)
    return teams



