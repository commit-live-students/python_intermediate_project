# %load q07_get_unique_teams_set/build.py
# Default imports
import csv
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'


def get_unique_teams_set():
    ipl_df=read_ipl_data_csv(path,dtype='|S50')
    team_1=set([x[3] for x in ipl_df[1:]])
    team_2=set([x[4] for x in ipl_df[1:]])
    union = team_1.union(team_2)    
    return (union)
get_unique_teams_set()



