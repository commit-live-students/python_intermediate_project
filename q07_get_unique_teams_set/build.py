# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np
path = "data/ipl_matches_small.csv"

def get_unique_teams_set():
    ipl_matches_array = np.genfromtxt(path,dtype='|S50', skip_header=1,delimiter = ',')
    teams_overall =ipl_matches_array[:,(3,4)]

    list_of_teams = []
    for i in teams_overall:
        list_of_teams.append(i[0])
        list_of_teams.append(i[1])

    #print(list_of_teams)
    list_unique_teams = np.unique(list_of_teams)
    set_unique_teams = set(list_unique_teams)
    return set_unique_teams

get_unique_teams_set()
