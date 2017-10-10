# Default imports
import numpy as np
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = "data/ipl_matches_small.csv"

def get_unique_teams_set():
    ipl_matches_array = read_ipl_data_csv(path,"|S50")
    teams =  ipl_matches_array[:,12]
    unique_teams =np.unique(teams)
    unique_team_set = set(unique_teams)
    return unique_team_set
