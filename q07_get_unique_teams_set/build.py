# Default imports
import numpy as np
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv

path = "data/ipl_matches_small.csv"

# Enter Code Here
def get_unique_teams_set():
    data = read_ipl_data_csv(path, dtype = '|S50')
    team1_uni = set(np.unique(data[:,3]))
    team2_uni = set(np.unique(data[:,4]))
    return  team1_uni | team2_uni
