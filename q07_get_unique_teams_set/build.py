# %load q07_get_unique_teams_set/build.py
# Default imports
import numpy as np
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

def get_unique_teams_set():
    m = read_ipl_data_csv(path,'|S50') #Called read_ipl_data function
    team1 = (m[0:,3]) #extracted data from team 1 col & stored
    team2 = (m[0:,4]) #extracted data from team 2 col & stored
    
    #teams = team1 | team2 #union alternative
    teams = np.union1d(team1,team2) #union of the set
    return set(teams) #return set


