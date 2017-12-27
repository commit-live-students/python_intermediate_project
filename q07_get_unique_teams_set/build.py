# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = "data/ipl_matches_small.csv"
import numpy as np
# Enter Code Here
def get_unique_teams_set():
    ipl_matches_array = np.genfromtxt(path,delimiter=',',dtype='|S50',skip_header=1)
    team1 = np.unique(ipl_matches_array[:,3])
    team2 = np.unique(ipl_matches_array[:,4])
    result = set(np.union1d(team1,team2))

    return result
#print get_unique_teams_set()
