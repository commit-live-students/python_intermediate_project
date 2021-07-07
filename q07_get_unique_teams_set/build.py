# %load q07_get_unique_teams_set/build.py
# Default imports
import numpy as np
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

def get_unique_teams_set():
    ipl_matches_array = np.genfromtxt(path, dtype=None, delimiter=',', skip_header=1,usecols=(3)) #read csv file
    ipl_matches_array = np.unique(ipl_matches_array,return_counts=True) #find unique values
    team1 = ipl_matches_array #saperate unique values and their counts
    set1 = set(team1[0])
    #print set1
    #print ''
    ipl_matches_array = np.genfromtxt(path, dtype=None, delimiter=',', skip_header=1,usecols=(4)) #read csv file
    ipl_matches_array = np.unique(ipl_matches_array,return_counts=True) #find unique values
    team2 = ipl_matches_array #saperate unique values and their counts
    set2 = set(team2[0])
    #print set2
    
    setPrime = set1.union(set2)
    return setPrime

