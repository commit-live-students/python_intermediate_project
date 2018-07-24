# %load q07_get_unique_teams_set/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'
import numpy as np

# Enter Code Here
def get_unique_teams_set():
    import csv
    ipl = []
    with open('data/ipl_matches_small.csv') as csvfile:
        reader = csv.reader(csvfile)
        for x in reader:
            ipl.append(x)
    header = tuple(ipl[0])        
    header1 = ipl[0]        
    team_1 = [x[3] for x in ipl[1:]]
    team_1 = set([x.encode('utf-8') for x in team_1])
    team_2 = [x[4] for x in ipl[1:]]
    team_2 = set([x.encode('utf-8') for x in team_2])
    team_1.union(team_2)
    teams = set(team_1.union(team_2))
    return teams






