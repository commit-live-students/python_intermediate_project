# %load q07_get_unique_teams_set/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np
path = 'data/ipl_matches_small.csv'
dtype='|S50'
# Enter Code Here

def get_unique_teams_set():
    ipl_matches_array=read_ipl_data_csv(path,dtype)
    team1=ipl_matches_array[:,3]
    team2=ipl_matches_array[:,4]
    teams_set=set(list(team1)+list(team2))
    return teams_set

get_unique_teams_set()



