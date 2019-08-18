# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np
path = "data/ipl_matches_small.csv"

# Enter Code Here
def get_unique_teams_set():
    data = read_ipl_data_csv(path,'|S50')
    uniq_team1 = np.unique(data[:,3])
    uniq_team2 = np.unique(data[:,4])
    uniq_teams = set(np.unique(np.union1d(uniq_team1, uniq_team2)))
    return uniq_teams
