# %load q07_get_unique_teams_set/build.py
# Default imports
import numpy as np
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_unique_teams_set():
    file_data = read_ipl_data_csv(path, dtype='|S50')
    team1 = set(file_data[:,3])
    team2 = set(file_data[:,4])
    set3 = team1.union(team2)
    return set3


