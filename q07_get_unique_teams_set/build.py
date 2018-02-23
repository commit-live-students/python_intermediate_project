import numpy as np
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = "data/ipl_matches_small.csv"

def get_unique_teams_set():
    ipl_data_arr = read_ipl_data_csv(path,'|S50')
    team1 = ipl_data_arr[:,3]
    team2 = ipl_data_arr[:,4]
    union_team = np.unique(np.union1d(team1,team2))
    return set(union_team)
#print get_unique_teams_set()
