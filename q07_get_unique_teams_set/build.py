# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = "data/ipl_matches_small.csv"
import numpy as np

def get_unique_teams_set():
    data = read_ipl_data_csv(path = path, dtype='|S50' )
    team1 = set(np.unique(data[:,[3]]))
    team2 = set(np.unique(data[:,[4]]))
    uniqueness = team1 | team2
    return uniqueness

get_unique_teams_set()
