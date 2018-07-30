# %load q07_get_unique_teams_set/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

def get_unique_teams_set():
    data  = read_ipl_data_csv(path,dtype = '|S50')
    team1 = set()
    team2 = set()
    for row in data:
        team1.add(row[3])
        team2.add(row[4])
    return team1.union(team2)

# Enter Code Here
#get_unique_teams_set()


