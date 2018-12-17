# %load q07_get_unique_teams_set/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

# Enter Code Here

def get_unique_teams_set():
    data = read_ipl_data_csv(path,'|S100')
    team1,team2 = data[:,3],data[:,4]
    return set.union(set(team1),set(team2))


