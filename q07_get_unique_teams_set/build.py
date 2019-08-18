# Default imports
import numpy as np
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = "data/ipl_matches_small.csv"

# Enter Code Here

def get_unique_teams_set():
    result = read_ipl_data_csv(path, dtype='|S50')
    team1 = result[0:,3]
    team1_final = np.unique(team1)
    team1_set = set(team1_final)

    team2 = result[0:,4]
    team2_final = np.unique(team2)
    team2_set = set(team2_final)

    final_teams = team1_set | team2_set
    return final_teams
