# %load q07_get_unique_teams_set/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'
import numpy as np
import pandas as pd
# Enter Code Here
ipl= pd.read_csv(path)
def get_unique_teams_set():
    ipl_matches_array=np.genfromtxt(path, delimiter=',',dtype='|S50',skip_header=1)
    team1 = set(ipl_matches_array[:,3])
    team2=set(ipl_matches_array[:,4])
    return team1.union(team2)

get_unique_teams_set()




