# %load q07_get_unique_teams_set/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = "data/ipl_matches_small.csv"

# Enter Code Here
import numpy as np
import pandas as pd
data = pd.read_csv(path)
def get_unique_teams_set():
    a = data['team1'].unique().tolist()
    b = data['team2'].unique().tolist()
    return set().union(a,b)
