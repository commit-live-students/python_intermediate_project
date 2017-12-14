# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = "data/ipl_matches_small.csv"

# Enter Code Here
import numpy as np
def get_unique_teams_set():
    ipl_data = read_ipl_data_csv(path=path,dtype='|S50')
    team1 = np.unique(ipl_data[:,3]) #unique values from column team1
    team2 = np.unique(ipl_data[:,4]) #unique values from column team2
    teams = np.union1d(team1, team2) #union the two results
    teams_set = set(teams)
    return teams_set

print get_unique_teams_set()
