# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = "data/ipl_matches_small.csv"
import numpy as np
import pandas as pd

def read_ipl_data_csv():
    a = np.genfromtxt(path, skip_header = 1, delimiter =',', dtype ='|S50')
    return a


def get_unique_teams_set():
    a = read_ipl_data_csv()
    team_1 = set(a[:,3])
    print team_1
    team_2 = set(a[:,4])
    print team_2
    #total_team_union = np.union1d(team_1,team_2)
    return team_1.union(team_2)

get_unique_teams_set()
# Enter Code Here
