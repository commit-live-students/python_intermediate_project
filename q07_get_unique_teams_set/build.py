# %load q07_get_unique_teams_set/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'
import pandas as pd 
# Enter Code Here
def get_unique_teams_set ():
    team1 = pd.DataFrame(read_ipl_data_csv('data/ipl_matches_small.csv','|S100'))[3]
    team2 = pd.DataFrame(read_ipl_data_csv('data/ipl_matches_small.csv','|S100'))[4]
    return set(team1).union(set(team2))



