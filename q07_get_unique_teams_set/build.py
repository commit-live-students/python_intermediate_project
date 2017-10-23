# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = "data/ipl_matches_small.csv"
import numpy as np

# Enter Code Here
def get_unique_teams_set():

    ipl_matches_array = read_ipl_data_csv(path, np.object)
    teams = [i[12] for i in ipl_matches_array]
    return set(teams)
