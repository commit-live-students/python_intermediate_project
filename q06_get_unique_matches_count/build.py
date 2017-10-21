# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'
import numpy as np
# Enter Code Here

def get_unique_matches_count():
    arr = np.genfromtxt('data/ipl_matches_small.csv', delimiter = ',', skip_header = 1, dtype = '|S50')
    matches = np.unique(arr[:, 0])
    return matches.size
