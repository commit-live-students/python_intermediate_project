# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = "data/ipl_matches_small.csv"

import numpy as np

def get_unique_teams_set():
    data = read_ipl_data_csv(path,'|S50')
    teams = data[:,3:5]
    return set(np.unique(teams))
# Enter Code Here
