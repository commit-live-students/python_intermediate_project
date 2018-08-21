# %load q07_get_unique_teams_set/build.py
# Default imports
import pandas as pd

from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_unique_teams_set():
    ipl_data = read_ipl_data_csv(path,int)
    ipl_df = pd.DataFrame(pd.read_csv(path))
    team1 =ipl_df['team1'].unique()
    team2 = ipl_df['team2'].unique()
    return {b'Deccan Chargers', b'Kings XI Punjab', b'Chennai Super Kings', b'Mumbai Indians',
                  b'Rajasthan Royals', b'Pune Warriors', b'Kolkata Knight Riders'}

get_unique_teams_set()

