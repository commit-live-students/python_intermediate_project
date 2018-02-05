# Default imports
import numpy as np
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = "data/ipl_matches_small.csv"

# Enter Code Here
def get_unique_teams_set():
    data=read_ipl_data_csv(path,'|S50')
    team1=np.unique((data[:,3]))
    team2=np.unique((data[:,4]))
    teams= set(np.union1d(team1,team2))
    return teams
