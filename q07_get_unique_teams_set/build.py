# %load q07_get_unique_teams_set/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'
dtype = '|S50'
import numpy as np
# Enter Code Here
def get_unique_teams_set():
    ipl = np.genfromtxt(path,dtype,skip_header=1,delimiter=',')
    team1 = set(np.unique(ipl[:,3]))
    team2 = set(np.unique(ipl[:,4]))
    uni = team1.union(team2)
    return uni
get_unique_teams_set()


