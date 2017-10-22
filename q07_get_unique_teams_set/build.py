# %load q07_get_unique_teams_set/build.py
# Default imports
# %load q07_get_unique_teams_set/build.py
# Default imports
import numpy as np
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = "data/ipl_matches_small.csv"

def get_unique_teams_set():
    ipl_matches_array = read_ipl_data_csv(path,dtype = '|S50')
    teams = set(np.unique(ipl_matches_array[:,3:5]))
    return teams
