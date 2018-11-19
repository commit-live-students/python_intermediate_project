# %load q07_get_unique_teams_set/build.py
# Default imports
import numpy as np
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_unique_teams_set():
    array = read_ipl_data_csv(path, dtype = '|S100')
    return set(np.unique(array[:, 3:5]))
get_unique_teams_set()


