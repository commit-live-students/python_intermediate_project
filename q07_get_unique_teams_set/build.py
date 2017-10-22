# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = "data/ipl_matches_small.csv"
import numpy as np

# Enter Code Here
def get_unique_teams_set():
    ipl_matches_array = read_ipl_data_csv(path,dtype='|S50')
    unique_teams = set(np.unique(ipl_matches_array[:,[3,4]]))
    #unique_teams = np.unique(ipl_matches_array[:,[3,4]])
    #print(unique_teams)
    #print(type(unique_teams))
    #print(np.unique(ipl_matches_array[:,[3,4]]))
    return unique_teams
#get_unique_teams_set()
