#%load q07_get_unique_teams_set/build.py/

import numpy as np

path='./data/ipl_matches_small.csv'

def get_unique_teams_set():
    arr=np.genfromtxt(path,delimiter=',',skip_header=1,dtype='|S25')

    #team1=arr[:,2:]
    
    team1=np.unique(arr[:,3],axis=0)
    team2=np.unique(arr[:,4],axis=0)

    uniqueteams=np.union1d(team1,team2)
    #Team=team1.union(team2)
    x=set(uniqueteams.flat)

#print(team1)
#print(team2)
#print(uniqueteams)    
    return (x)



get_unique_teams_set()









