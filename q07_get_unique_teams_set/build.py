# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = "data/ipl_matches_small.csv"
import numpy as np
# Enter Code Here
def get_unique_teams_set():
    data_index = read_ipl_data_csv(path,dtype=np.str)
    new_data_1 = data_index[:,3]
    team_1 = np.unique(new_data_1)
    team1 = set(team_1)
    #team1 = team_1.size
    #print type(team1)
    new_data_2 = data_index[:,4]
    team_2 = np.unique(new_data_2)
    team2 = set(team_2)
    #print team_2
    team1_team2 = team1 | team2
    return team1_team2
print get_unique_teams_set()
