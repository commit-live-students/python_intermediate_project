# %load q07_get_unique_teams_set/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'
import numpy as np
# Enter Code Here
def read_ipl_data_csv():
    data=np.genfromtxt(path,delimiter=',',dtype=None)
    return data

def get_unique_teams_set():
    data= read_ipl_data_csv()
    team11=data[1:,3]
    team1=np.unique(team11)
    team22=data[1:,4]
    team2=np.unique(team22)

    good=np.union1d(team1,team2)
    list1=good.tolist()
    set1=set(list1)
    return set1
   
    
get_unique_teams_set()    
    
    




