# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = "data/ipl_matches_small.csv"
dtype='|S50'

def get_unique_teams_set():
    ipl_matches_array = read_ipl_data_csv(path, dtype)
    team1_set = set(ipl_matches_array[:, 3]) #Set method to get unordered collection with no duplicate elements
    team2_set = set(ipl_matches_array[:, 4])
    return team1_set.union(team2_set)
