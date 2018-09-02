# %load q07_get_unique_teams_set/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

# Enter Code Here
import pandas as pd
column_1 = set()
column_2 = set()
def get_unique_teams_set():
    df = pd.read_csv(path)
    for i in range(0,len(df['match_code'])):
        team1 = df['team1'][i]
        team2 = df['team2'][i]
        if team1 not in column_1:
            column_1.add(team1)
            
        if team2 not in column_2:
            column_2.add(team2)
    
    return column_1 | column_2





