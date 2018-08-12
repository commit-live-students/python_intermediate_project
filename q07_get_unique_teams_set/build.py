# %load q07_get_unique_teams_set/build.py
# Default imports
import pandas as pd
import numpy as np
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv


# Enter Code Here
def get_unique_teams_set():
    path = 'data/ipl_matches_small.csv'
    #sets = {}
    team1 = read_ipl_data_csv(path, 'str')
    #team1 = pd.read_csv(path,delimiter=',') #  
    print(team1)
    #team1 = np.genfromtxt(path, dtype='|S50', skip_header=1, delimiter=',')
    
    #team1 = read_ipl_data_csv(path) #, '|S50')
    #print(team1.head())
    set1 = set(team1[:,3])
    set2 = set(team1[:,4])
    res_set = set1.union(set2)
    
    return set1.union(set2)
    
get_unique_teams_set()


