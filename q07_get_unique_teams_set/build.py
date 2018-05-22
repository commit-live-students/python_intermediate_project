# %load q07_get_unique_teams_set/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

# Enter Code Here

def get_unique_teams_set():
    team_1 = set()
    team_2 = set()
    
    data = read_ipl_data_csv(path,'|S50')

    for i in range(0,data.shape[0]):
        if data[i][3] not in team_1:
                team_1.add(data[i][3])
        if data[i][4] not in team_2:
                team_2.add(data[i][4])
        
    return (team_1.union(team_2))


