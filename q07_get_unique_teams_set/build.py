# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = "data/ipl_matches_small.csv"

# Enter Code Here
def get_unique_teams_set():
    ipl_matches_array = read_ipl_data_csv(path, dtype='|S50')
    teams = [col[3] for col in ipl_matches_array]
    teams.extend([col[4] for col in ipl_matches_array])
    return set(teams)
