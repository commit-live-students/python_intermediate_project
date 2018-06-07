# %load q07_get_unique_teams_set/build.py
# Default imports
import numpy as np
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'
dtype = '|S50'
# Enter Code Here
def get_unique_teams_set():
    my_data = np.genfromtxt(path,dtype,skip_header=1,delimiter=',')
    team1 = set(my_data[:,3])
    team2 = set(my_data[:,4])
    return set(team1.union(team2))
get_unique_teams_set()

