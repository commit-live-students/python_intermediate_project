# Default imports
import numpy as np
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = "data/ipl_matches_small.csv"

def get_unique_teams_set():
    ipl_matches = read_ipl_data_csv(path,'|S50')
    team_set_a = np.unique(ipl_matches[:,3])
    team_set_b = np.unique(ipl_matches[:,4])
    final_teams = len(np.union1d(team_set_a,team_set_b))
    return final_teams
# Enter Code Here
