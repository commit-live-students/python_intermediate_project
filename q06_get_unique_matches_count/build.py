# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

# Enter Code Here
# Enter Code Here
import numpy as np

ipl_matches_array = read_ipl_data_csv(path, dtype = '|S50')
matches = []

def get_unique_matches_count():
    for i in ipl_matches_array:
        matches.append(i[0])
    matches2= np.array(matches)
    matches_unique = np.unique(matches2)
    matches_count = np.size(matches_unique)
    return matches_count
