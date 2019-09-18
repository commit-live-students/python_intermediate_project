# %load q07_get_unique_teams_set/build.py
# Default imports
import numpy as np
import pandas as pd
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = "data/ipl_matches_small.csv"

# Enter Code Here
def read_ipl_data_csv(path, dtype):
    data = np.genfromtxt(path, delimiter=',', dtype=dtype, skip_header=1)
    return data

def get_unique_teams_set():
    data = read_ipl_data_csv(path, dtype='|S50')
    total_team1 = set(data[:,3] )
    total_team2 = set(data[:,4] )
    return total_team1.union(total_team2)

get_unique_teams_set()
