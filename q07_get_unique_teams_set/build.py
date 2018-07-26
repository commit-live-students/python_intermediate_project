# %load q07_get_unique_teams_set/build.py
# Default imports
import numpy as np
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_unique_teams_set():
    ipl_matches_array = read_ipl_data_csv(path,'|S50')
    unique_team1 = np.unique(ipl_matches_array[:,3])
    unique_team2 = np.unique(ipl_matches_array[:,4])
    unique_teams = set(np.concatenate((unique_team1, unique_team2),axis=0))
    
    return unique_teams


