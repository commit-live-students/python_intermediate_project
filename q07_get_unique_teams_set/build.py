# %load q07_get_unique_teams_set/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

import numpy as np
import csv 
 
def get_unique_teams_set():
    ipl=[]
    team = []
    ipl=read_ipl_data_csv(path,'|S50')
    header=tuple(ipl[0])  
    
    team=set(np.unique([x[3:5] for x in ipl[1:]]))
       # team2=np.unique([x[4] for x in ipl[1:]])
    
        


    return team

print(get_unique_teams_set())






