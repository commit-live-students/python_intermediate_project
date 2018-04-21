import numpy as np
def get_unique_teams_set():
    read_ipl_data_csv=np.genfromtxt('./data/ipl_matches_small.csv',delimiter=',',dtype='|S100',skip_header=1)
    team1=np.unique(read_ipl_data_csv[:,3]).astype('|S50')
    team2=np.unique(read_ipl_data_csv[:,4])
    t1=set(team1)
    t2=set(team2)
    return t1.union(t2)

get_unique_teams_set()

