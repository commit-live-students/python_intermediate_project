# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np
path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_unique_matches_count():
    data = read_ipl_data_csv(path , '|S50')
    match_id = data[:,0]
    unique_match_id = np.unique(match_id)
    ipl_matches_array = len(unique_match_id)
    return ipl_matches_array


print get_unique_matches_count()
