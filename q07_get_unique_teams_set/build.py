# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = "data/ipl_matches_small.csv"
import numpy as np

# Enter Code Here

def get_unique_teams_set ():
    ipl_matches_data = read_ipl_data_csv (path,'|S50')
    unique_teams_1 = np.unique(ipl_matches_data[1:, 3])
    unique_teams_2 = np.unique(ipl_matches_data[1:, 4])
    teams_1 = set(unique_teams_1)
    teams_2 = set(unique_teams_2)
    return teams_1.union(teams_2)
