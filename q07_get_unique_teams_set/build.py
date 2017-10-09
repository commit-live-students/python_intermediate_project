# %load q07_get_unique_teams_set/build.py
# Default imports
import numpy as np
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = "data/ipl_matches_small.csv"

def get_unique_teams_set():

    ipl_matches_array = read_ipl_data_csv(path, "|S50")
    team1 = ipl_matches_array[:,3]

    team2 = ipl_matches_array[:,4]

    team1 = np.concatenate((team1,team2))

    uniquearray1 = np.unique(team1)
    finalarray = set(uniquearray1)


    #uniquearray = np.unique(ipl_matches_array[:,0])

    #return len(uniquearray)
    return finalarray


# Enter Code Here
