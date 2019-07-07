# %load q07_get_unique_teams_set/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

# Enter Code Here
import numpy as np
import csv

def get_unique_teams_set ():
    ipl=[]
    ipl=read_ipl_data_csv(path,dtype = type(float))
    header = tuple(ipl[0])
    team1= []
    team2=[]
    teams = []
    
    team1 = set(np.unique([x[3] for x in ipl[1:]]))
    team2 = set(np.unique([x[4] for x in ipl[1:]])) 
    teams = team1.union(team2)           
    return teams

    
    
get_unique_teams_set()


