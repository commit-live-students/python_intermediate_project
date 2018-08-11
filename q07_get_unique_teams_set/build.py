# %load q07_get_unique_teams_set/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np
path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_unique_teams_set():
    ipl_data = read_ipl_data_csv(path, np.string_)
    team1 = ipl_data[:, 3]
    team2 = ipl_data[:, 4]

    return set(np.union1d(team1, team2))
r = get_unique_teams_set()
r


