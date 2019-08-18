# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

path = 'data/ipl_matches_small.csv'

# Enter Code Here

def get_total_extras():
    ipl_matches_array = np.genfromtxt('./data/ipl_matches_small.csv', dtype='|S50', delimiter=',')
    extras = ipl_matches_array[1:,17].astype(np.int)
    return np.sum(extras)
