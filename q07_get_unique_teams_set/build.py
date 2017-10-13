# %load q07_get_unique_teams_set/build.py
# Default imports
import numpy as np
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = "data/ipl_matches_small.csv"
temp=[]
# Enter Code Here
def get_unique_teams_set():
    data = read_ipl_data_csv(path,dtype='|S50')
    unique_team1 , team1_fre= np.unique(temp[:,3],return_counts=True)
    unique_team2 , team2_fre= np.unique(temp[:,4],return_counts=True)
    unique_teams={member for member in np.append(unique_team2,unique_team1)}

    return unique_teams
