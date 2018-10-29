# %load q07_get_unique_teams_set/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'
import numpy as np

# Enter Code Here
def get_unique_teams_set():
    ipl_data = read_ipl_data_csv(path, dtype='S50')
    teams_data = ipl_data[:,[3,4]]

    teams_un = set(np.unique(teams_data))
    return teams_un
    #print(np.unique(teams_data))
    #teams = len(np.unique(teams_data))
    #return teams
get_unique_teams_set()    


