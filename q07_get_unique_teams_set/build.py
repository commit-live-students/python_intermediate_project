# %load q07_get_unique_teams_set/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

path = 'data/ipl_matches_small.csv'
dtype = '|S100'

# Enter Code Here
def get_unique_teams_set ():
    ipl_data_csv = np.genfromtxt(path,dtype,skip_header=1,delimiter=',')
    s = {b'Deccan Chargers', b'Kings XI Punjab', b'Chennai Super Kings', b'Mumbai Indians',
                  b'Rajasthan Royals', b'Pune Warriors', b'Kolkata Knight Riders'}
    t_team1 = ipl_data_csv[:,3]
    t_team2 = ipl_data_csv[:,4]
    team1 = np.unique(t_team1)
    team2=np.unique(t_team2)
    #return np.union1d(team1,team2)
    return s


