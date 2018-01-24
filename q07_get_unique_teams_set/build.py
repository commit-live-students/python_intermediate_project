# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = "data/ipl_matches_small.csv"

# Enter Code Here
def get_unique_teams_set():
    new = read_ipl_data_csv(path,dtype='|S50')
    team1 = set(new[:,3])
    team2 = set(new[:,4])
    #print (team1,team2)
    team_union = team1|team2
    return team_union
