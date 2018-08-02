# %load q07_get_unique_teams_set/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'
ipl = read_ipl_data_csv(path,'|S50')
def get_unique_teams_set():
    team1 = []
    team2 = []
    for x in ipl:
        team1.append(x[3])
    for x in ipl:
        team2.append(x[4])
    teams = team1 + team2   
    return set(teams)
get_unique_teams_set()



