import numpy as np
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = "data/ipl_matches_small.csv"
def get_unique_teams_set():
    ipl_teams1=[]
    ipl_teams2=[]
    ipl_match=read_ipl_data_csv(path=path,dtype='|S50')
    for matches in ipl_match:
        ipl_teams1.append(matches[3])
        ipl_teams2.append(matches[4])
    unique_team1=set(ipl_teams1)
    unique_team2=set(ipl_teams2)
    unique_teams=set(unique_team1 | unique_team2)
    return unique_teams
