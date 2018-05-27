# %load q07_get_unique_teams_set/build.py
# Default imports
import numpy as np
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_unique_teams_set():
    ipl_matches_array = np.genfromtxt(path,dtype='|S50', skip_header = 1,delimiter=',')
    team1 = np.unique(ipl_matches_array [:,3])
    team2 = np.unique(ipl_matches_array [:,4])
    teams = np.union1d(team1,team2)
    teamsset = set(teams)
    return teamsset
get_unique_teams_set()


