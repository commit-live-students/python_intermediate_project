# %load q07_get_unique_teams_set/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

# Enter Code Here
import numpy as np
from numpy import genfromtxt
def get_unique_teams_set():
    
    def read_ipl_data_csv(path, dtype= '|S50'):
        ipl_data= np.genfromtxt('./data/ipl_matches_small.csv', delimiter=',')
        team_set= set(ipl_data)
        team1= np.unique(team_set, team1)
        team2= np.unique(team_set, team2)
        np.union(team1,team2)
        return team1,team2
        
        
    
    
    

get_unique_teams_set()


