# Default imports
import numpy as np
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = "data/ipl_matches_small.csv"
# Enter Code Here
def get_unique_teams_set():
    ipl_matches= read_ipl_data_csv(path,'|S50')
    return set(np.union1d (np.unique(ipl_matches[0:,3]), np.unique(ipl_matches[0:,4])))
