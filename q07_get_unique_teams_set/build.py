# %load q07_get_unique_teams_set/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'
import numpy as np
import csv

# Enter Code Here
def get_unique_teams_set():
    with open(path, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        headers = next(reader)
        data = list(reader)
        ar1=np.array(data)
        team1=set(ar1[:,3].astype('|S50'))
        team2=set(ar1[:,4].astype('|S50'))
        unio=team1.union(team2)
        return unio

get_unique_teams_set()
path = 'data/ipl_matches_small.csv'
import numpy as np
import csv
with open(path, 'r') as f:
    reader = csv.reader(f, delimiter=',')
    headers = next(reader)
    data = list(reader)
    ar1=np.array(data)
    team1=set(np.unique(ar1[0:,3:4]))
    team2=set(np.unique(ar1[0:,4:5]))
    print(team1)
    print(team2)
    print (type((team1.union(team2))))
    



