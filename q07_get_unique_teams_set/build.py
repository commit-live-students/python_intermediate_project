# Default imports
import numpy as np
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_unique_teams_set():
    new = read_ipl_data_csv(path, dtype='|S50')
    q = np.unique(new[:,3])
    s = np.unique(new[:,4])
    team_1 = set(q)
    team_2 = set(s)
    unique_matches = team_1 | team_2
    return unique_matches

get_unique_teams_set()
