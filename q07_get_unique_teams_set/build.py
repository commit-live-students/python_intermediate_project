# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = "data/ipl_matches_small.csv"

# Enter Code Here
def get_unique_teams_set():
    iplmatch = read_ipl_data_csv(path,dtype='|S50')
    team1=set()
    team2=set()
    for i in iplmatch:
        team1.add(i[3])
        team2.add(i[4])
    team_unique=team1|team2
    return team_unique
