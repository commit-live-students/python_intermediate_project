# Default imports
import numpy as np
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = "./data/ipl_matches_small.csv"

def get_unique_matches_count():
    ipl_mini = read_ipl_data_csv(path = path, dtype='|S100' )
    match_id = np.unique(ipl_mini[:,[0]])
    ipl_matches_array = np.size(match_id)
    return ipl_matches_array
get_unique_matches_count()
