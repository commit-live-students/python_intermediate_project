# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = "data/ipl_matches_small.csv"

def get_unique_teams_set():
    data = read_ipl_data_csv(path,dtype='|S50')
    team1 = team2 = set()
    for d in data:
        team1.add(d[3])
        team2.add(d[4])
    return team1.union(team2)
