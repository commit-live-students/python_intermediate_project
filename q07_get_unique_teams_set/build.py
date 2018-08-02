# %load q07_get_unique_teams_set/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_unique_teams_set():
    read_ipl_data = read_ipl_data_csv('data/ipl_matches_small.csv',dtype='|S50')
    team1 = set(read_ipl_data[:,3])
    team2 = set(read_ipl_data[:,4])
    return team1.union(team2)
    
    
    
    

