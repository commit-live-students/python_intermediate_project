# %load q07_get_unique_teams_set/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np
path = './data/ipl_matches_small.csv'
dtype ='|S50'
def get_unique_teams_set():
    ipl_matches=read_ipl_data_csv(path,dtype)
    team1=set(ipl_matches[:,3].astype('|S50'))
    team2=set(ipl_matches[:,4].astype('|S50'))
    union_teams=team1.union(team2)
    return(union_teams)
# Enter Code Here

import numpy as np
path = './data/ipl_matches_small.csv'
dtype ='|S50'
ipl_matches=np.genfromtxt(path,dtype,skip_header=1,delimiter=',')
team1=set(ipl_matches[:,3].astype('|S100'))
team2=set(ipl_matches[:,4].astype('|S100'))
union_teams=team1.union(team2)
print(ipl_matches[:3])




