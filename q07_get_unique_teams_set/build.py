# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = "data/ipl_matches_small.csv"
import numpy as np
# Enter Code Here
def get_unique_teams_set():

    data = read_ipl_data_csv(path,'|S50')
    match_codes = data[:,12:13]
    unique_count = set(np.unique(match_codes).flatten())
    print unique_count
    return unique_count

get_unique_teams_set()
