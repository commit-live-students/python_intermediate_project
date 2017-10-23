# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'
import numpy as np

# Enter Code Here
def get_unique_matches_count():
    ipl_matches_array = read_ipl_data_csv(path, np.float64)
    match_codes = [i[0] for i in ipl_matches_array]
    return len(set(match_codes))

print get_unique_matches_count()
