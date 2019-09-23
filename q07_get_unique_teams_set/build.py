# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = "data/ipl_matches_small.csv"

# Enter Code Here
import numpy as np
dtype = '|S50'
def get_unique_teams_set():
    var = read_ipl_data_csv(path,dtype)
    team1 = set(var[:,3])
    team2 = set(var[:,4])
    return team1.union(team2)

print (get_unique_teams_set())
