import numpy as np
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = "data/ipl_matches_small.csv"


def get_unique_teams_set():
    teams = np.genfromtxt(path, dtype = '|S50', delimiter = ",", skip_header = 1, usecols = (3, 4))
    team1 = (teams[:, :1])
    team2 = (teams[:, 1:2])
    total_team = np.union1d(team1, team2)
    #total_team = np.hstack((team1, team2))
    total_team = set(total_team)
    return (total_team)
print get_unique_teams_set()
