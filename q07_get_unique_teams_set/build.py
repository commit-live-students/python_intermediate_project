from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

path = 'data/ipl_matches_small.csv'

def get_unique_teams_set():
    ipl_data = read_ipl_data_csv(path,'|S50')
    team1 = ipl_data[:,3]
    set1=set(team1)
    team2 = ipl_data[:,4]
    set2 = set(team2)
    return set1.union(set2)

get_unique_teams_set()

