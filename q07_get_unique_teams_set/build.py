# %load q07_get_unique_teams_set/build.py
# Default imports
import numpy as np
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_unique_teams_set():
    
    ipl_matches_array = read_ipl_data_csv(path, dtype = '|S50')
    team1 = set(ipl_matches_array[:,3])
    team2 = set(ipl_matches_array[:,4])
    union_teams = team1 | team2
    
    return union_teams
    
    





