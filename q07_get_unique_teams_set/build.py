# %load q07_get_unique_teams_set/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'
import numpy as np

# Enter Code Here
def get_unique_teams_set():
    ipl_matches_array = np.genfromtxt('./data/ipl_matches_small.csv', dtype='|S50', delimiter=',', skip_header=1)
    unique_teams1 = np.unique(ipl_matches_array[:, 3])
    unique_teams2 = np.unique(ipl_matches_array[:, 4])
    teams_union = np.union1d(unique_teams1, unique_teams2)
    return teams_union


