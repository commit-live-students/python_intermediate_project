# Default imports
import numpy as np
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = "data/ipl_matches_small.csv"

# Enter Code Here
def get_unique_teams_set():
    ipl_match_array = read_ipl_data_csv(path,dtype='|S200')
    team1 =np.unique(ipl_match_array[:,3])
    team2 =np.unique(ipl_match_array[:,4])
    ipl_team_set = set(np.union1d(team1, team2))
    return ipl_team_set
