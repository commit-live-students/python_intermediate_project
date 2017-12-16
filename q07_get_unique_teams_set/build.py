# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import pandas as pd
path = "data/ipl_matches_small.csv"

# Enter Code Here
def get_unique_teams_set():
    data = pd.read_csv(path,dtype='|S50')
    team1 = set(data['team1'])
    team2 = set(data['team2'])
    teams = team1 | team2
    return teams
