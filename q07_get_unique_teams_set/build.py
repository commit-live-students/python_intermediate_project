# %load q07_get_unique_teams_set/build.py
# Default imports
import numpy as np
from operator import add
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'
# Enter Code Here
data= np.genfromtxt(path, dtype='|S50', delimiter= ',', skip_header=1)

def get_unique_teams_set():
    team1= list(np.unique(data[:,3]))
    team2= list(np.unique(data[:,4]))
    set_teams= set(team1+team2)
    return set_teams








