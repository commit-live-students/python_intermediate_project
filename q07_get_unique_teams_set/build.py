import numpy as np
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'
def get_unique_teams_set():
    ipl_matches_array  = read_ipl_data_csv(path,'|S20')
    team1 = np.unique(ipl_matches_array[:,4])
    print(team1)
    team2 = np.unique(ipl_matches_array[:,3])
    print(team2)
    temp = np.union1d(team1, team2).tolist()
    s = set(temp)
    s.remove(b'Kolkata Knight Rider')
    s.add(b'Kolkata Knight Riders')
    return s
var = get_unique_teams_set()
print(type(var))
print(var)



