# %load q07_get_unique_teams_set/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

def get_unique_teams_set():
    ipl_matches_array = read_ipl_data_csv(path, dtype='|S50')
    team1_set = set(ipl_matches_array[:, 3])
    team2_set = set(ipl_matches_array[:, 4])
    return team1_set.union(team2_set)
