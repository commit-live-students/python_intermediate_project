# %load q07_get_unique_teams_set/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'
import numpy as np
# Enter Code Here

def get_unique_teams_set():
    ipl= read_ipl_data_csv(path,'|S50')
    team1=ipl[:,3]
    team2=ipl[:,4]
    set1=set(team1)
    set2=set(team2)
    return set1.union(set2)



