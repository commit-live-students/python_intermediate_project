# %load q07_get_unique_teams_set/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_unique_teams_set():
    array = read_ipl_data_csv('data/ipl_matches_small.csv', dtype = '|S50')
    team_1 = set(array[:,3])
    team_2 = set(array[:,4])
    team_union = team_1.union(team_2)
    print (team_union)
    return team_1.union(team_2)
get_unique_teams_set()


