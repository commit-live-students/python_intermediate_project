# Default imports
import numpy as np
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = "data/ipl_matches_small.csv"

def get_unique_teams_set():
    actual_data = read_ipl_data_csv(path, dtype='|S50')
    unique_team1 = np.unique(actual_data[:,3:4])
    unique_team2 = np.unique(actual_data[:,4:5])
    combined_unique = np.hstack((unique_team1,unique_team2))
    totally_unique = set(combined_unique)
    return totally_unique

print get_unique_teams_set()
