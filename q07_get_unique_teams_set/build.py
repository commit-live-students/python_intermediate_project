# %load q07_get_unique_teams_set/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_unique_teams_set():
    data= read_ipl_data_csv(path,dtype='|S50')
    team1 = set(data[:,3])
    team2 = set(data[:,4])
    teamUnion = set().union(team1,team2)
    return teamUnion
get_unique_teams_set()



