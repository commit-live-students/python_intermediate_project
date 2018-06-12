# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = "data/ipl_matches_small.csv"

import numpy as np

def get_unique_teams_set():
    ipl_matches_array = read_ipl_data_csv(path, dtype='|S50')
    teams = np.unique(ipl_matches_array[:,(3,4)])
    output =set()
    for team in teams:
        output.add(team)
    return output
    
