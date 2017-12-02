# Default imports
import numpy as np
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

# Enter Code Here

def get_unique_matches_count():
    ipl_matches_array = read_ipl_data_csv('data/ipl_matches_small.csv', dtype='|S50')
    return len(np.unique(ar=ipl_matches_array[:,0]))
