# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = "data/ipl_matches_small.csv"

# Enter Code Here
def get_unique_teams_set():
    data = read_ipl_data_csv(path,dtype='|S50')
    team1,team2 = [],[]
    for i in data:
        team1.append(i[3])
        team2.append(i[4])
    team1 = set(team1)
    team2 = set(team2)
    union = (team1 | team2)
    return union

#print get_unique_teams_set()
