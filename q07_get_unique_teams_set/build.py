# %load q07_get_unique_teams_set/build.py
# Default imports

import numpy as np
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_unique_teams_set():
    
    #np.set_printoptions(threshold = np.nan)
    matches = read_ipl_data_csv(path, dtype = '|S50')
    
    team1 = list(matches[:,3])
    team2 = list(matches[:,4])
    
    return set(team2 + team1)
    
get_unique_teams_set()



