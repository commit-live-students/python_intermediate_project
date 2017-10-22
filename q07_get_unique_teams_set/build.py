# %load q07_get_unique_teams_set/build.py
# Default imports
import numpy as np
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = "data/ipl_matches_small.csv"

def get_unique_teams_set():
    team_set=set()
    ipl_match_array=read_ipl_data_csv(path,'|S50')
    team1=np.unique(ipl_match_array[:,3])
    team2=np.unique(ipl_match_array[:,4])

    for elements in team1:
        team_set.add(elements)
    for elements in team2:
        team_set.add(elements)

    return team_set

get_unique_teams_set()

# Enter Code Here
