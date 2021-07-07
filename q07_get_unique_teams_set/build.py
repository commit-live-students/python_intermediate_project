# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

path = "data/ipl_matches_small.csv"

def get_unique_teams_set():

    data = read_ipl_data_csv(path,'|S50')
    team1 = data[:,3]
    unique_team1 = np.unique(team1)
    team2 = data[:,4]
    unique_team2 = np.unique(team2)
    teams = np.union1d(unique_team1,unique_team2)
    return set(teams)
