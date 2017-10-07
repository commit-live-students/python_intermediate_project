# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np
path = "data/ipl_matches_small.csv"

# Enter Code Here
def get_unique_teams_set():
    data = read_ipl_data_csv(path,'|S50')
    #teams = np.unique(data[:,3:5])
    teams = np.unique(data[:,3:5])
    team = []
    for i in teams:
        team.append(i)
    return set(team)

get_unique_teams_set()
