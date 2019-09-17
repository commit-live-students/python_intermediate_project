# Default imports
import numpy as np
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = "data/ipl_matches_small.csv"

# Enter Code Here
def get_unique_teams_set():
    read_data = read_ipl_data_csv(path,dtype = '|S50')
    t1 = read_data[:,3]
    t2 = read_data[:,4]
    team1 = set(t1)
    team2 = set(t2)
    unique_teams = team1.union(team2) #team1 | team2
    return unique_teams
