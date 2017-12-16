# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
#path = "data/ipl_matches_small.csv"
path = '/home/snmjack/Workspace/code/python_intermediate_project/data/ipl_matches_small.csv'
#/home/snmjack/.atom/.commit-live/code/python_intermediate_project/data
import numpy as np
# Enter Code Here

def get_unique_teams_set():
    #unique_teams = ()
    data = read_ipl_data_csv(path,dtype='|S50')
    #print data
    team1 = set(data[:,3])
    team2 = set(data[:,4])
    #team1 = np.unique(data[:,3])
    #print team1
    #team2 = np.unique(data[:,4])
    #print team2
    #print type(team2)
    #unique_teams = [team1] unioun [team2]
    unique_teams = team1.union(team2)
    #print unique_teams
    #print type(unique_teams)

    return unique_teams

#et_unique_teams_set()
