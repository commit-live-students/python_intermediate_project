# Default imports
import numpy as np
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = "data/ipl_matches_small.csv"

# Enter Code Here
def get_unique_teams_set():
    narray = read_ipl_data_csv(path, '|S50')
    team1 = np.unique(narray[:,3]) #team1 unique values
    #print team1
    team2 =np.unique(narray[:,4]) #unique team names from team2
    #print team2
    teams = set(team1) | set(team2)
    #print teams
    #print type(teams)
    return teams

#get_unique_teams_set()
