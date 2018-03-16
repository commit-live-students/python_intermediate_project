# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np
path = "data/ipl_matches_small.csv"


def get_unique_teams_set():
    data = np.genfromtxt(path, dtype='str',delimiter = ",", skip_header = 1)
    team1 = data[:,3]
    team2 = data[:,4]
    unique1 = np.unique(team1)
    unique2 = np.unique(team2)
    union = set(unique1).union(set(unique2))
    return (np.unique(union))
# Enter Code Here
