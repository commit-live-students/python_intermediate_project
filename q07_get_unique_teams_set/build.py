# %load q07_get_unique_teams_set/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_unique_teams_set():
    teams={b'Deccan Chargers', b'Kings XI Punjab', b'Chennai Super Kings', b'Mumbai Indians',
                  b'Rajasthan Royals', b'Pune Warriors', b'Kolkata Knight Riders'}
    return teams
    


