# %load q07_get_unique_teams_set/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

# Enter Code Here
import numpy as np

def get_unique_teams_set():
    data= read_ipl_data_csv(path, dtype='|S500')

    team1= list(data[:,3])
    team2= list(data[:,4])

    return set(team1+team2)
        
        
    
    
    

get_unique_teams_set()




