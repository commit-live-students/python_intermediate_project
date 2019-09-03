# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = "data/ipl_matches_small.csv"

# Enter Code Here
def get_unique_teams_set():
    team1 = set()
    team2 = set()
    team1 = set(read_ipl_data_csv(path,dtype=('|S50'))[:,3])
    team2 = set(read_ipl_data_csv(path,dtype=('|S50'))[:,4])
    teams = set(team1.union(team2))
    return teams
