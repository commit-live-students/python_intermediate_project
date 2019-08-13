# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = "data/ipl_matches_small.csv"

# Enter Code Here
import numpy as np

unique_teams = read_ipl_data_csv(path, dtype = '|S50')
matches = []

def get_unique_teams_set():
    for i in unique_teams:
        matches.append(i[3])
        matches.append(i[4])
    #matches2= np.array(matches)
    matches_unique = set(matches)
    return matches_unique

teams = get_unique_teams_set()
