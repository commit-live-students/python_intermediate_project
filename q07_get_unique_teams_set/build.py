# %load q07_get_unique_teams_set/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'
dtype='|S100'
# Enter Code Here
def get_unique_teams_set():
    ipl_data = read_ipl_data_csv(path, dtype)
    team_1 = set(ipl_data[:, 3])
    team_2 = set(ipl_data[:, 4])
    team_union = team_1.union(team_2)
    return team_union
    
get_unique_teams_set()

