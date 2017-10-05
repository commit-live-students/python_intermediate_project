import pprint
import numpy as np
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'
s = set()
# Enter Code Here
def get_unique_teams_set():
    ipl_matches_array  = np.genfromtxt('./data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=",")
    team1 = ipl_matches_array[:,3]
    team2 = ipl_matches_array[:,4]
    for val in team1:
        s.add(val)
    for val in team2:
        s.add(val)
    return s
