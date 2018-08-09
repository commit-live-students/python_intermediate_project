# %load q07_get_unique_teams_set/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'
import numpy as np
# Enter Code Here
def get_unique_teams_set():
    a = read_ipl_data_csv(path,dtype=str)
    team1 = set(a[:,3])
    team2 = set(a[:,4])
    return set().union(team1,team2)
get_unique_teams_set()


