# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = "data/ipl_matches_small.csv"
import numpy as np

def get_unique_teams_set():
    data = read_ipl_data_csv(path, dtype = '|S50')
    team1_name = data[:, 3]
    team1 = np.unique(team1_name)

    team2_name = data[:, 4]
    team2 = np.unique(team2_name)

    c =  set(team1)
    d = set(team2)

    union =  c | d

    return union

print get_unique_teams_set()
# Enter Code Here
