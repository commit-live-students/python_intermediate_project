# %load q07_get_unique_teams_set/build.py
# Default imports
import numpy as np
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_unique_teams_set():
    team1=[]
    team2=[]
    teams=[]
    data=read_ipl_data_csv(path,'|S50')
   # print(data)
    for i in data:
        team1.append(i[3])
        team2.append(i[4])
    #print(type(np.unique(team1)))
    teams=list(np.unique(team1))+list(np.unique(team2))
    return(set(teams))
#get_unique_teams_set()

