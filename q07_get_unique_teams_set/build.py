# %load q07_get_unique_teams_set/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'
def get_unique_teams_set():
    ipl_matches_array = read_ipl_data_csv('data/ipl_matches_small.csv', dtype='|S50')
    team1 = set(ipl_matches_array[:,3])
    team2 = set(ipl_matches_array[:,4])
    teams = team1.union(team2)
    return teams
get_unique_teams_set()
# Enter Code Here


