# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = "data/ipl_matches_small.csv"

# Enter Code Here

import numpy as np

def get_unique_teams_set():
    def read_ipl_data_csv(file_path, dtype='|S50'):
        ipl_matches_array = np.genfromtxt(file_path,delimiter=',',dtype='|S50',skip_header=1)
        return ipl_matches_array

    team1_unique_count= np.unique(read_ipl_data_csv(path)[0:,3])

    team2_unique_count= np.unique(read_ipl_data_csv(path)[0:,4])

    final_result = set(np.union1d(team1_unique_count,team2_unique_count))

    return final_result
