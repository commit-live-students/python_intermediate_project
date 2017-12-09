import numpy as np
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = "data/ipl_matches_small.csv"

def get_unique_teams_set():
    a = read_ipl_data_csv (path,dtype='|S50')
    team1=np.unique(a[...,3])
    team2=np.unique(a[...,4])
    teams = np.union1d(team1,team2)
    #print type(teams)
    return set(teams)
