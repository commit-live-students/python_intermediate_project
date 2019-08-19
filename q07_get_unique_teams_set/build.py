# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = "data/ipl_matches_small.csv"
import numpy as np

# Enter Code Here
def get_unique_teams_set():
    ipl_matches_array=read_ipl_data_csv(path,'|S50')
    team1= np.unique(ipl_matches_array[:,3])
    team2= np.unique(ipl_matches_array[:,4])
    val= set(np.union1d(team1,team2))
    #print type(val)
    return val
get_unique_teams_set()
