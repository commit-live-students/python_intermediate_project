# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = "data/ipl_matches_small.csv"

# Enter Code Here
def get_unique_teams_set():
    data = read_ipl_data_csv(path, dtype="|S50")
    team_1 = data[:,3]
    team_2 = data[:,4]
    l = set(team_1)
    l.update(team_2)
    return l
