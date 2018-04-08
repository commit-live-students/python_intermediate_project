# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = "data/ipl_matches_small.csv"
import numpy as np
# Enter Code Here
dtype='|S50'
def get_unique_teams_set():
    data=read_ipl_data_csv(path,dtype)
    team1= data[:,3].astype(np.str)
    team2= data[:,4].astype(np.str)
    variable=np.union1d(team1,team2)
    return np.all(variable)
